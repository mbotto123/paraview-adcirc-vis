# Script to add location labels, compatible with zoomToHoustonBeaumont3D script
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
viewUpScale = 0.05

textHouston = Text(registrationName='TextHouston')
textHoustonDisplay = Show(textHouston, renderView1, 'TextSourceRepresentation')
textHoustonDisplay.TextPropMode = 'Flagpole Actor'
textHouston.Text = 'Houston'
textHoustonDisplay.FontSize = 40
textHoustonDisplay.Bold = 1
textHoustonDisplay.Shadow = 1
textHoustonDisplay.BasePosition = [-95.3698, 29.7604, 0.0]
textHoustonDisplay.TopPosition = [-95.3698 + viewUp[0]*viewUpScale, 29.7604 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textGalveston = Text(registrationName='TextGalveston')
textGalvestonDisplay = Show(textGalveston, renderView1, 'TextSourceRepresentation')
textGalvestonDisplay.TextPropMode = 'Flagpole Actor'
textGalveston.Text = 'Galveston'
textGalvestonDisplay.FontSize = 40
textGalvestonDisplay.Bold = 1
textGalvestonDisplay.Shadow = 1
textGalvestonDisplay.BasePosition = [-94.7977, 29.3013, 0.0]
textGalvestonDisplay.TopPosition = [-94.7977 + viewUp[0]*viewUpScale, 29.3013 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textBolivarP = Text(registrationName='TextBolivarP')
textBolivarPDisplay = Show(textBolivarP, renderView1, 'TextSourceRepresentation')
textBolivarPDisplay.TextPropMode = 'Flagpole Actor'
textBolivarP.Text = 'Bolivar Peninsula'
textBolivarPDisplay.FontSize = 40
textBolivarPDisplay.Bold = 1
textBolivarPDisplay.Shadow = 1
textBolivarPDisplay.BasePosition = [-94.5799, 29.4783, 0.0]
textBolivarPDisplay.TopPosition = [-94.5799 + viewUp[0]*viewUpScale, 29.4783 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textBeaumont = Text(registrationName='TextBeaumont')
textBeaumontDisplay = Show(textBeaumont, renderView1, 'TextSourceRepresentation')
textBeaumontDisplay.TextPropMode = 'Flagpole Actor'
textBeaumont.Text = 'Beaumont'
textBeaumontDisplay.FontSize = 40
textBeaumontDisplay.Bold = 1
textBeaumontDisplay.Shadow = 1
textBeaumontDisplay.BasePosition = [-94.1266, 30.0802, 0.0]
textBeaumontDisplay.TopPosition = [-94.1266 + viewUp[0]*viewUpScale, 30.0802 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.08
