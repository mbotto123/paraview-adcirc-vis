# Script to add location labels, compatible with zoomToCorpusChristi3D script
# coordinates of text base positions were obtained from lat/long values for each location

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

cam = GetActiveCamera()
# get the viewUp vector for the camera
# a scalar multiple of this vector will be added to each bottom coordinate of the text flagpoles
# to obtain a top coordinate that ensures the text will face the camera
# if this vector is not added, the text will not properly face the camera
viewUp = cam.GetViewUp()
viewUpScale = 0.075

text1 = Text()
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
text1Display.TextPropMode = 'Flagpole Actor'
text1.Text = 'Corpus Christi'
text1Display.FontSize = 45
text1Display.Bold = 1
text1Display.Shadow = 1
text1Display.BasePosition = [-97.3964, 27.8006, 0.0]
text1Display.TopPosition = [-97.3964 + viewUp[0]*viewUpScale, 27.8006 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text2 = Text()
text2Display = Show(text2, renderView1, 'TextSourceRepresentation')
text2Display.TextPropMode = 'Flagpole Actor'
text2.Text = 'Port Aransas'
text2Display.FontSize = 45
text2Display.Bold = 1
text2Display.Shadow = 1
text2Display.BasePosition = [-97.0611, 27.8339, 0.0]
text2Display.TopPosition = [-97.0611 + viewUp[0]*viewUpScale, 27.8339 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text3 = Text()
text3Display = Show(text3, renderView1, 'TextSourceRepresentation')
text3Display.TextPropMode = 'Flagpole Actor'
text3.Text = 'Rockport'
text3Display.FontSize = 45
text3Display.Bold = 1
text3Display.Shadow = 1
text3Display.BasePosition = [-97.0544, 28.0206, 0.0]
text3Display.TopPosition = [-97.0544 + viewUp[0]*viewUpScale, 28.0206 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.08
