# Script to add location labels, compatible with zoomToHoustonBeaumont3D script

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

cam = GetActiveCamera()
viewUp = cam.GetViewUp()
viewUpScale = 0.05

text1 = Text()
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
text1Display.TextPropMode = 'Flagpole Actor'
text1.Text = 'Houston'
text1Display.FontSize = 45
text1Display.Bold = 1
text1Display.Shadow = 1
text1Display.BasePosition = [-95.3698, 29.7604, 0.0]
text1Display.TopPosition = [-95.3698 + viewUp[0]*viewUpScale, 29.7604 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text2 = Text()
text2Display = Show(text2, renderView1, 'TextSourceRepresentation')
text2Display.TextPropMode = 'Flagpole Actor'
text2.Text = 'Galveston'
text2Display.FontSize = 45
text2Display.Bold = 1
text2Display.Shadow = 1
text2Display.BasePosition = [-94.7977, 29.3013, 0.0]
text2Display.TopPosition = [-94.7977 + viewUp[0]*viewUpScale, 29.3013 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text3 = Text()
text3Display = Show(text3, renderView1, 'TextSourceRepresentation')
text3Display.TextPropMode = 'Flagpole Actor'
text3.Text = 'Bolivar Peninsula'
text3Display.FontSize = 45
text3Display.Bold = 1
text3Display.Shadow = 1
text3Display.BasePosition = [-94.5799, 29.4783, 0.0]
text3Display.TopPosition = [-94.5799 + viewUp[0]*viewUpScale, 29.4783 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text4 = Text()
text4Display = Show(text4, renderView1, 'TextSourceRepresentation')
text4Display.TextPropMode = 'Flagpole Actor'
text4.Text = 'Beaumont'
text4Display.FontSize = 40
text4Display.Bold = 1
text4Display.Shadow = 1
text4Display.BasePosition = [-94.1266, 30.0802, 0.0]
text4Display.TopPosition = [-94.1266 + viewUp[0]*viewUpScale, 30.0802 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.08
