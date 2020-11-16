# Script to zoom in to an ADCIRC domain, focusing on a 3D view of the LA-TX border
# including Port Arthur, TX; Beaumont, TX; Lake Charles, LA; Cameron, LA; Hackberry, LA
# Prerequisites: blueBrownGreenBathyTopo color map must be loaded into ParaView

# This script can handle a ParaView visualization made from following ADCIRC output files: 
# maxele.63.nc, fort.63.nc, or combined fort.63.nc and fort.74.nc

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1441, 755]

# get layout
layout1 = GetLayout()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera()

# set the camera position
camera = GetActiveCamera()
camera.SetFocalPoint(-85.68415868826808, 109.73542352640422, -66.23746845234106)
camera.SetPosition(-93.77671940167772, 28.84649367662483, 0.9698449093857261)
camera.SetViewUp(-0.00935122333748162, 0.6395860096329778, 0.7686626639195226)
Render()

# find source
if (FindSource('fort.63.nc_fort.74.nc.xmf')) is not None:
	generalSource = FindSource('fort.63.nc_fort.74.nc.xmf')
elif (FindSource('fort.63.nc.xmf')) is not None:
	generalSource = FindSource('fort.63.nc.xmf')
elif (FindSource('maxele.63.nc.xmf')) is not None:
	generalSource = FindSource('maxele.63.nc.xmf')

#### This section defines the color mapping properties for bathymetry/topography ####
# get color transfer function/color map for 'BathymetricDepth'
bathymetricDepthLUT = GetColorTransferFunction('BathymetricDepth')
bathymetricDepthLUT.RGBPoints = [-106.09833, 0.231373, 0.298039, 0.752941, 3938.042335, 0.865003, 0.865003, 0.865003, 7982.183, 0.705882, 0.0156863, 0.14902]
bathymetricDepthLUT.ScalarRangeInitialized = 1.0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
bathymetricDepthLUT.ApplyPreset('blueBrownGreenBathyTopo', False)

# get opacity transfer function/opacity map for 'BathymetricDepth'
bathymetricDepthPWF = GetOpacityTransferFunction('BathymetricDepth')
bathymetricDepthPWF.Points = [-106.09833, 0.0, 0.5, 0.0, 7982.183, 1.0, 0.5, 0.0]
bathymetricDepthPWF.ScalarRangeInitialized = 1

# Rescale transfer function
bathymetricDepthPWF.RescaleTransferFunction(-20.0, 100.0)

# Properties modified on bathymetricDepthLUT
bathymetricDepthLUT.AutomaticRescaleRangeMode = 'Never'

# get color legend/bar for bathymetricDepthLUT in view renderView1
bathymetricDepthLUTColorBar = GetScalarBar(bathymetricDepthLUT, renderView1)
bathymetricDepthLUTColorBar.ComponentTitle = ''
bathymetricDepthLUTColorBar.AutoOrient = 0
bathymetricDepthLUTColorBar.Orientation = 'Vertical'
bathymetricDepthLUTColorBar.WindowLocation = 'AnyLocation'
bathymetricDepthLUTColorBar.Position = [0.014129077029839513, 0.7101986754966899]
bathymetricDepthLUTColorBar.Title = 'Bathymetry/Topography (m)'
bathymetricDepthLUTColorBar.AddRangeLabels = 0
bathymetricDepthLUTColorBar.ScalarBarLength = 0.25
bathymetricDepthLUTColorBar.ScalarBarThickness = 16
#### end definition of bathymetry/topography color map properties ####

#### This section defines scalar warp properties to produce an exaggerated 3D effect based on bathymetry/topography values ####
warpByScalar1 = WarpByScalar(Input=generalSource)
warpByScalar1.Scalars = ['POINTS', 'BathymetricDepth']
warpByScalar1.ScaleFactor = -0.001
warpByScalar1Display = Show(warpByScalar1, renderView1, 'UnstructuredGridRepresentation')
Hide(generalSource, renderView1)
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)
renderView1.Update()
bathymetricDepthLUTColorBar.WindowLocation = 'AnyLocation'
bathymetricDepthLUTColorBar.Position = [0.014129077029839513, 0.7101986754966899]
#### end definition of bathymetry/topography scalar warp properties ####

#### This section defines the color mapping properties for water surface elevation ####
# create a new 'Threshold' to filter out ADCIRC missing values for water surface elevation
threshold1 = Threshold(Input=generalSource)
if (FindSource('maxele.63.nc.xmf')) is not None:
	threshold1.Scalars = ['POINTS', 'zeta_max']
else:
	threshold1.Scalars = ['POINTS', 'zeta']
	
threshold1.ThresholdRange = [-9999.0, 7982.183]

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', threshold1.Scalars[1]))

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'zeta' or 'zeta_max'
zetaLUT = GetColorTransferFunction(threshold1.Scalars[1])
zetaLUT.RGBPoints = [-2.651, 0.231373, 0.298039, 0.752941, 0.8777015514658117, 0.865003, 0.865003, 0.865003, 4.406403102931623, 0.705882, 0.0156863, 0.14902]
zetaLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'zeta' or 'zeta_max'
zetaPWF = GetOpacityTransferFunction(threshold1.Scalars[1])
zetaPWF.Points = [-2.651, 0.0, 0.5, 0.0, 4.406403102931623, 1.0, 0.5, 0.0]
zetaPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
zetaLUT.ApplyPreset('erdc_rainbow_dark', True)

# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, 5.0)

# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, 5.0)

zetaLUT.AutomaticRescaleRangeMode = 'Never'

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.9

# get color legend/bar for zetaLUT in view renderView1
zetaLUTColorBar = GetScalarBar(zetaLUT, renderView1)
zetaLUTColorBar.ComponentTitle = ''
zetaLUTColorBar.AutoOrient = 0
zetaLUTColorBar.Orientation = 'Vertical'
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.07702984038861965, 0.7101986754966899]
zetaLUTColorBar.Title = 'Water Surface Elevation (m)'
zetaLUTColorBar.AddRangeLabels = 0
zetaLUTColorBar.ScalarBarLength = 0.25
zetaLUTColorBar.ScalarBarThickness = 16
#### end definition of water surface elevation color map properties ####

#### This section defines scalar warp properties to produce an exaggerated 3D effect based on water surface elevation values ####
warpByScalar2 = WarpByScalar(Input=threshold1)
warpByScalar2.Scalars = ['POINTS', threshold1.Scalars[1]]
warpByScalar2.ScaleFactor = 0.001
warpByScalar2Display = Show(warpByScalar2, renderView1, 'UnstructuredGridRepresentation')
Hide(threshold1, renderView1)
warpByScalar2Display.SetScalarBarVisibility(renderView1, True)
#ColorBy(warpByScalar2Display, ('POINTS', threshold1.Scalars[1]))
renderView1.Update()
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.07702984038861965, 0.7101986754966899]

# get display properties
warpByScalar2Display = GetDisplayProperties(warpByScalar2, view=renderView1)
# set scalar coloring
ColorBy(warpByScalar2Display, ('POINTS', threshold1.Scalars[1]))
# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(bathymetricDepthLUT, renderView1)
# rescale color and/or opacity maps used to include current data range
warpByScalar2Display.RescaleTransferFunctionToDataRange(True, False)
# show color bar/color legend
warpByScalar2Display.SetScalarBarVisibility(renderView1, True)
# change scalar bar placement
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.07702984038861965, 0.7101986754966899]
# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, 5.0)
# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, 5.0)
#### end definition of water surface elevation scalar warp properties ####

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0