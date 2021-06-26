# Script to add wind vectors to a general 2D view of the LA-TX coast

# This script must be used with a ParaView visualization made from combined fort.63.nc and fort.74.nc data
# the XDMF file to be opened with ParaView should be named like this: fort.63.nc_fort.74.nc.xmf

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')
generalSource = FindSource('fort.63.nc_fort.74.nc.xmf')

# create a new 'Surface Vectors'
surfaceVectors1 = SurfaceVectors(Input=generalSource)
surfaceVectors1.SelectInputVectors = ['POINTS', 'windVel']
surfaceVectors1Display = Show(surfaceVectors1, renderView1, 'UnstructuredGridRepresentation')

# create a new 'Glyph'
glyph1 = Glyph(Input=surfaceVectors1, GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'windVel']
glyph1.GlyphTransform = 'Transform2'
glyph1.ScaleArray = ['POINTS', 'windVel']
# This scale factor is intended for hurricane-level winds; it will be too small for normal winds
glyph1.ScaleFactor = 0.01
glyph1.MaximumNumberOfSamplePoints = 10000
glyph1.GlyphType.ShaftRadius = 0.02
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'

# Filter out wind vectors on dry nodes
threshold2 = Threshold(Input=glyph1)
threshold2.Scalars = ['POINTS', 'zeta']
threshold2.ThresholdRange = [-9999.0, 7877.455]

threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')
ColorBy(threshold2Display, None)

# update the view to ensure updated data information
renderView1.Update()