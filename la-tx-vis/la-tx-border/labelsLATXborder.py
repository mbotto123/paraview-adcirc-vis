#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

cam = GetActiveCamera()
viewUp = cam.GetViewUp()
viewUpScale = 0.075

text1 = Text()
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
text1Display.TextPropMode = 'Flagpole Actor'
text1.Text = 'Cameron'
text1Display.FontSize = 38
text1Display.Bold = 1
text1Display.Shadow = 1
text1Display.BasePosition = [-93.3252, 29.7977, 0.0]
text1Display.TopPosition = [-93.3252 + viewUp[0]*viewUpScale, 29.7977 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text2 = Text()
text2Display = Show(text2, renderView1, 'TextSourceRepresentation')
text2Display.TextPropMode = 'Flagpole Actor'
text2.Text = 'Port Arthur'
text2Display.FontSize = 38
text2Display.Bold = 1
text2Display.Shadow = 1
text2Display.BasePosition = [-93.9399, 29.885, 0.0]
text2Display.TopPosition = [-93.9399 + viewUp[0]*viewUpScale, 29.885 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text3 = Text()
text3Display = Show(text3, renderView1, 'TextSourceRepresentation')
text3Display.TextPropMode = 'Flagpole Actor'
text3.Text = 'Lake Charles'
text3Display.FontSize = 38
text3Display.Bold = 1
text3Display.Shadow = 1
text3Display.BasePosition = [-93.2174, 30.2266, 0.0]
text3Display.TopPosition = [-93.2174 + viewUp[0]*viewUpScale, 30.2266 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text4 = Text()
text4Display = Show(text4, renderView1, 'TextSourceRepresentation')
text4Display.TextPropMode = 'Flagpole Actor'
text4.Text = 'Hackberry'
text4Display.FontSize = 38
text4Display.Bold = 1
text4Display.Shadow = 1
text4Display.BasePosition = [-93.3421, 29.996, 0.0]
text4Display.TopPosition = [-93.3421 + viewUp[0]*viewUpScale, 29.996 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

text5 = Text()
text5Display = Show(text5, renderView1, 'TextSourceRepresentation')
text5Display.TextPropMode = 'Flagpole Actor'
text5.Text = 'Beaumont'
text5Display.FontSize = 38
text5Display.Bold = 1
text5Display.Shadow = 1
text5Display.BasePosition = [-94.1266, 30.0802, 0.0]
text5Display.TopPosition = [-94.1266 + viewUp[0]*viewUpScale, 30.0802 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.15
