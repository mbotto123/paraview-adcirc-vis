#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(Input=generalSource)

# Properties modified on annotateTimeFilter1
annotateTimeFilter1.Format = 'Time: %.2f days'
annotateTimeFilter1.Scale = 1.157407407e-05

# show data in view
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 11

