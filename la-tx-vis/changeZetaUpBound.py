# Script to change the upper bound for the water surface elevation color map
# Prompts the user for input through the ParaView GUI

# Can handle a ParaView visualization made from following ADCIRC output files: 
# maxele.63.nc, fort.63.nc, or combined fort.63.nc and fort.74.nc

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

uBound = input()
uBound = float(uBound)

# get color transfer function/color map for 'zeta' or 'zeta_max'
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaLUT = GetColorTransferFunction('zeta_max')
else:
	zetaLUT = GetColorTransferFunction('zeta')

# Rescale transfer function
zetaLUT.RescaleTransferFunction(0.0, uBound)

# get opacity transfer function/opacity map for 'zeta' or 'zeta_max'
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaPWF = GetOpacityTransferFunction('zeta_max')
else:
	zetaPWF = GetOpacityTransferFunction('zeta')


# Rescale transfer function
zetaPWF.RescaleTransferFunction(0.0, uBound)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).