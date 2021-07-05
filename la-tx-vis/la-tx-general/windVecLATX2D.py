# Script to add wind vectors to a general 2D view of the LA-TX coast

# This script must be used with a ParaView visualization made from combined fort.63.nc and fort.74.nc data
# the XDMF file to be opened with ParaView should be named like this: fort.63.nc_fort.74.nc.xmf

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')
generalSource = FindSource('fort.63.nc_fort.74.nc.xmf')

# SurfaceVectors filter processes wind vector data for input to the Glyph filter later
windSurfaceVec = SurfaceVectors(registrationName='WindSurfaceVec',Input=generalSource)
windSurfaceVec.SelectInputVectors = ['POINTS', 'windVel']
windSurfaceVecDisplay = Show(windSurfaceVec, renderView1, 'UnstructuredGridRepresentation')

# Create Glyph filter to display the vectors
# 3D arrow Glyph used for compatibility with billboard text labels
windVecGlyphs = Glyph(registrationName='WindVecGlyph',Input=windSurfaceVec, GlyphType='Arrow')
windVecGlyphs.OrientationArray = ['POINTS', 'windVel']
windVecGlyphs.GlyphTransform = 'Transform2'
windVecGlyphs.ScaleArray = ['POINTS', 'windVel']
# This scale factor is intended for hurricane-level winds; it will be too small for normal winds
windVecGlyphs.ScaleFactor = 0.01
windVecGlyphs.MaximumNumberOfSamplePoints = 10000
windVecGlyphs.GlyphType.ShaftRadius = 0.02
windVecGlyphs.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'

# Filter out wind vectors on dry nodes
windVecThreshold = Threshold(registrationName='WindVecThreshold',Input=windVecGlyphs)
windVecThreshold.Scalars = ['POINTS', 'zeta']
windVecThreshold.ThresholdRange = [-9999.0, 7877.455]

windVecThresholdDisplay = Show(windVecThreshold, renderView1, 'UnstructuredGridRepresentation')
ColorBy(windVecThresholdDisplay, None)

# Update render view with all changes at once
renderView1.Update()
