# Script to zoom in to an ADCIRC domain, focusing on a 3D view that includes the Galveston-Houston area and Beaumont
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
camera.SetFocalPoint(-94.73016732588835, 32.43587279283372, -2.4045719277885382)
camera.SetPosition(-94.38805750256448, 27.833096493571567, 1.446393338273202)
camera.SetViewUp(0.013093331933432064, 0.642206844249245, 0.7664195547207202)
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
bathymetricDepthLUTColorBar.Orientation = 'Horizontal'
bathymetricDepthLUTColorBar.WindowLocation = 'AnyLocation'
bathymetricDepthLUTColorBar.Position = [0.3596160472851709, 0.9142926335143605]
bathymetricDepthLUTColorBar.Title = 'Bathymetry/Topography (m)'
bathymetricDepthLUTColorBar.AddRangeLabels = 0
bathymetricDepthLUTColorBar.ScalarBarLength = 0.19
bathymetricDepthLUTColorBar.LabelFontSize = 12
bathymetricDepthLUTColorBar.ScalarBarThickness = 15
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
bathymetricDepthLUTColorBar.Position = [0.3596160472851709, 0.9142926335143605]
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

# get opacity transfer function/opacity map for 'zeta' or 'zeta_max'
zetaPWF = GetOpacityTransferFunction(threshold1.Scalars[1])

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
zetaLUTColorBar.Orientation = 'Horizontal'
zetaLUTColorBar.WindowLocation = 'AnyLocation'
zetaLUTColorBar.Position = [0.5791451099571648, 0.9142926335143605]
zetaLUTColorBar.Title = 'Water Surface Elevation (m)'
zetaLUTColorBar.AddRangeLabels = 0
zetaLUTColorBar.ScalarBarLength = 0.19
zetaLUTColorBar.LabelFontSize = 12
zetaLUTColorBar.ScalarBarThickness = 15
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
zetaLUTColorBar.Position = [0.5791451099571648, 0.9142926335143605] 

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
zetaLUTColorBar.Position = [0.5791451099571648, 0.9142926335143605] 
# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, 5.0)
# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, 5.0)

# Opacity/lighting properties
warpByScalar2Display.Opacity = 0.95
warpByScalar2Display.Diffuse = 0.9
#### end definition of water surface elevation scalar warp properties ####

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0
