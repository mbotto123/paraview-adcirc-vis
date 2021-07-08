# Script to add location labels, compatible with zoomToLATXborder3D script
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

textCameron = Text(registrationName='TextCameron')
textCameronDisplay = Show(textCameron, renderView1, 'TextSourceRepresentation')
textCameronDisplay.TextPropMode = 'Flagpole Actor'
textCameron.Text = 'Cameron'
textCameronDisplay.FontSize = 38
textCameronDisplay.Bold = 1
textCameronDisplay.Shadow = 1
textCameronDisplay.BasePosition = [-93.3252, 29.7977, 0.0]
textCameronDisplay.TopPosition = [-93.3252 + viewUp[0]*viewUpScale, 29.7977 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textPtArthur = Text(registrationName='TextPtArthur')
textPtArthurDisplay = Show(textPtArthur, renderView1, 'TextSourceRepresentation')
textPtArthurDisplay.TextPropMode = 'Flagpole Actor'
textPtArthur.Text = 'Port Arthur'
textPtArthurDisplay.FontSize = 38
textPtArthurDisplay.Bold = 1
textPtArthurDisplay.Shadow = 1
textPtArthurDisplay.BasePosition = [-93.9399, 29.885, 0.0]
textPtArthurDisplay.TopPosition = [-93.9399 + viewUp[0]*viewUpScale, 29.885 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textLakeCharles = Text(registrationName='TextLakeCharles')
textLakeCharlesDisplay = Show(textLakeCharles, renderView1, 'TextSourceRepresentation')
textLakeCharlesDisplay.TextPropMode = 'Flagpole Actor'
textLakeCharles.Text = 'Lake Charles'
textLakeCharlesDisplay.FontSize = 38
textLakeCharlesDisplay.Bold = 1
textLakeCharlesDisplay.Shadow = 1
textLakeCharlesDisplay.BasePosition = [-93.2174, 30.2266, 0.0]
textLakeCharlesDisplay.TopPosition = [-93.2174 + viewUp[0]*viewUpScale, 30.2266 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textHackberry = Text(registrationName='TextHackberry')
textHackberryDisplay = Show(textHackberry, renderView1, 'TextSourceRepresentation')
textHackberryDisplay.TextPropMode = 'Flagpole Actor'
textHackberry.Text = 'Hackberry'
textHackberryDisplay.FontSize = 38
textHackberryDisplay.Bold = 1
textHackberryDisplay.Shadow = 1
textHackberryDisplay.BasePosition = [-93.3421, 29.996, 0.0]
textHackberryDisplay.TopPosition = [-93.3421 + viewUp[0]*viewUpScale, 29.996 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textBeaumont = Text(registrationName='TextBeaumont')
textBeaumontDisplay = Show(textBeaumont, renderView1, 'TextSourceRepresentation')
textBeaumontDisplay.TextPropMode = 'Flagpole Actor'
textBeaumont.Text = 'Beaumont'
textBeaumontDisplay.FontSize = 38
textBeaumontDisplay.Bold = 1
textBeaumontDisplay.Shadow = 1
textBeaumontDisplay.BasePosition = [-94.1266, 30.0802, 0.0]
textBeaumontDisplay.TopPosition = [-94.1266 + viewUp[0]*viewUpScale, 30.0802 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.15
