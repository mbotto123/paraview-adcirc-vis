# trace generated using paraview version 5.8.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

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

camera = GetActiveCamera()
camera.SetFocalPoint(-92.13150887352528, 28.58515932960801, -95.18622433474408)
camera.SetPosition(-92.13150887352528, 28.58515932960801, 9.100680396002447)
camera.SetViewUp(0.0, 1.0, 0.0)
Render()

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

# find source
generalSource = FindSource('maxele.63.nc.xmf')

# create a new 'Threshold'
threshold1 = Threshold(Input=generalSource)
threshold1.Scalars = ['POINTS', 'zeta_max']
threshold1.ThresholdRange = [-9999.0, 7982.183]

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', 'zeta_max'))

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'zeta_max'
zeta_maxLUT = GetColorTransferFunction('zeta_max')
zeta_maxLUT.RGBPoints = [-2.651, 0.231373, 0.298039, 0.752941, 0.8777015514658117, 0.865003, 0.865003, 0.865003, 4.406403102931623, 0.705882, 0.0156863, 0.14902]
zeta_maxLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'zeta_max'
zeta_maxPWF = GetOpacityTransferFunction('zeta_max')
zeta_maxPWF.Points = [-2.651, 0.0, 0.5, 0.0, 4.406403102931623, 1.0, 0.5, 0.0]
zeta_maxPWF.ScalarRangeInitialized = 1

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
zeta_maxLUT.ApplyPreset('erdc_rainbow_dark', True)

# Rescale transfer function
zeta_maxLUT.RescaleTransferFunction(0.0, 5.0)

# Rescale transfer function
zeta_maxPWF.RescaleTransferFunction(0.0, 5.0)

zeta_maxLUT.AutomaticRescaleRangeMode = 'Never'

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.9

# get color legend/bar for zeta_maxLUT in view renderView1
zeta_maxLUTColorBar = GetScalarBar(zeta_maxLUT, renderView1)
zeta_maxLUTColorBar.ComponentTitle = ''
zeta_maxLUTColorBar.AutoOrient = 0
zeta_maxLUTColorBar.Orientation = 'Horizontal'
zeta_maxLUTColorBar.WindowLocation = 'AnyLocation'
zeta_maxLUTColorBar.Position = [0.3976405274115199, 0.805298013245033]
zeta_maxLUTColorBar.Title = 'Water Surface Elevation (m)'
zeta_maxLUTColorBar.AddRangeLabels = 0
zeta_maxLUTColorBar.ScalarBarLength = 0.25

# get color legend/bar for bathymetricDepthLUT in view renderView1
bathymetricDepthLUTColorBar = GetScalarBar(bathymetricDepthLUT, renderView1)
bathymetricDepthLUTColorBar.ComponentTitle = ''
bathymetricDepthLUTColorBar.AutoOrient = 0
bathymetricDepthLUTColorBar.Orientation = 'Horizontal'
bathymetricDepthLUTColorBar.WindowLocation = 'AnyLocation'
bathymetricDepthLUTColorBar.Position = [0.3976405274115199, 0.9064900682461972]
bathymetricDepthLUTColorBar.Title = 'Bathymetry/Topography (m)'
bathymetricDepthLUTColorBar.AddRangeLabels = 0
bathymetricDepthLUTColorBar.ScalarBarLength = 0.25
