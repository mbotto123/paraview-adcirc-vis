# trace generated using paraview version 5.8.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

uBound = input()
uBound = float(uBound)

# get color transfer function/color map for 'zeta'
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaLUT = GetColorTransferFunction('zeta_max')
else:
	zetaLUT = GetColorTransferFunction('zeta')

# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, uBound)

# get opacity transfer function/opacity map for 'zeta'
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaPWF = GetOpacityTransferFunction('zeta_max')
else:
	zetaPWF = GetOpacityTransferFunction('zeta')


# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, uBound)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).