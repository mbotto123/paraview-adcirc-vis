# Script to un-discretize water surface elevation color map
# Compatible with any ADCIRC output file that contains bathmetry/topography and water surface elevation 

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get color transfer function/color map for 'zeta'
if (FindSource('maxele.63.nc.xmf')) is not None:
	zetaLUT = GetColorTransferFunction('zeta_max')
else:
	zetaLUT = GetColorTransferFunction('zeta')

# Discretize color maps by reducing the number of table values
zetaLUT.NumberOfTableValues = 256
