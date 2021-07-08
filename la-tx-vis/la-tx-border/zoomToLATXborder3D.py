# Script to zoom in to an ADCIRC domain, focusing on a 3D view of the LA-TX border
# including Port Arthur, TX; Beaumont, TX; Lake Charles, LA; Cameron, LA; Hackberry, LA
# Prerequisites: blueBrownGreenBathyTopo and RdYlBu_Brewer color maps must be loaded into ParaView

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
bathyTopoScalarWarp = WarpByScalar(registrationName='BathyTopoWarp',Input=generalSource)
bathyTopoScalarWarp.Scalars = ['POINTS', 'BathymetricDepth']
bathyTopoScalarWarp.ScaleFactor = -0.001
bathyTopoScalarWarpDisplay = Show(bathyTopoScalarWarp, renderView1, 'UnstructuredGridRepresentation')
Hide(generalSource, renderView1)
bathyTopoScalarWarpDisplay.SetScalarBarVisibility(renderView1, True)
renderView1.Update()
bathymetricDepthLUTColorBar.WindowLocation = 'AnyLocation'
bathymetricDepthLUTColorBar.Position = [0.014129077029839513, 0.7101986754966899]
#### end definition of bathymetry/topography scalar warp properties ####

#### This section defines the color mapping properties for water surface elevation ####
# create a new 'Threshold' to filter out ADCIRC missing values for water surface elevation
zetaThreshold = Threshold(registrationName='WaterSurfEleThreshold',Input=generalSource)
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaThreshold.Scalars = ['POINTS', 'zeta_max']
else:
	zetaThreshold.Scalars = ['POINTS', 'zeta']
	
zetaThreshold.ThresholdRange = [-9999.0, 7982.183]

# show data in view
zetaThresholdDisplay = Show(zetaThreshold, renderView1, 'UnstructuredGridRepresentation')

# set scalar coloring
ColorBy(zetaThresholdDisplay, ('POINTS', zetaThreshold.Scalars[1]))

# rescale color and/or opacity maps used to include current data range
zetaThresholdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
zetaThresholdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'zeta' or 'zeta_max'
zetaLUT = GetColorTransferFunction(zetaThreshold.Scalars[1])

# get opacity transfer function/opacity map for 'zeta' or 'zeta_max'
zetaPWF = GetOpacityTransferFunction(zetaThreshold.Scalars[1])

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
zetaLUT.ApplyPreset('RdYlBu_Brewer', True)

# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, 5.0)

# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, 5.0)

zetaLUT.AutomaticRescaleRangeMode = 'Never'

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
zetaScalarWarp = WarpByScalar(registrationName='WaterSurfEleWarp',Input=zetaThreshold)
zetaScalarWarp.Scalars = ['POINTS', zetaThreshold.Scalars[1]]
zetaScalarWarp.ScaleFactor = 0.001
zetaScalarWarpDisplay = Show(zetaScalarWarp, renderView1, 'UnstructuredGridRepresentation')
Hide(zetaThreshold, renderView1)
zetaScalarWarpDisplay.SetScalarBarVisibility(renderView1, True)
#ColorBy(zetaScalarWarpDisplay, ('POINTS', zetaThreshold.Scalars[1]))
renderView1.Update()
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.07702984038861965, 0.7101986754966899]

# get display properties
zetaScalarWarpDisplay = GetDisplayProperties(zetaScalarWarp, view=renderView1)
# set scalar coloring
ColorBy(zetaScalarWarpDisplay, ('POINTS', zetaThreshold.Scalars[1]))
# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(bathymetricDepthLUT, renderView1)
# rescale color and/or opacity maps used to include current data range
zetaScalarWarpDisplay.RescaleTransferFunctionToDataRange(True, False)
# show color bar/color legend
zetaScalarWarpDisplay.SetScalarBarVisibility(renderView1, True)
# change scalar bar placement
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.07702984038861965, 0.7101986754966899]
# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, 5.0)
# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, 5.0)

# Opacity/lighting properties
zetaScalarWarpDisplay.Opacity = 0.95
zetaScalarWarpDisplay.Diffuse = 0.9
#### end definition of water surface elevation scalar warp properties ####

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0
