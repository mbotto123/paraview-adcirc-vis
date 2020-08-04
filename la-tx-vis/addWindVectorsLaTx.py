#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Surface Vectors'
surfaceVectors1 = SurfaceVectors(Input=threshold1)
surfaceVectors1.SelectInputVectors = ['POINTS', 'windVel']
surfaceVectors1Display = Show(surfaceVectors1, renderView1, 'UnstructuredGridRepresentation')

# create a new 'Glyph'
glyph1 = Glyph(Input=surfaceVectors1, GlyphType='2D Glyph')
glyph1.OrientationArray = ['POINTS', 'windVel']
glyph1.GlyphTransform = 'Transform2'
glyph1.ScaleArray = ['POINTS', 'windVel']
glyph1.ScaleFactor = 0.01
glyph1.MaximumNumberOfSamplePoints = 10000

glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# turn off scalar coloring
ColorBy(glyph1Display, None)

# Properties modified on glyph1
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'

# update the view to ensure updated data information
renderView1.Update()