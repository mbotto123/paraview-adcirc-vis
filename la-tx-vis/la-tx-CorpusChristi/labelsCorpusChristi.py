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

textCorpusChristi = Text(registrationName='TextCorpusChristi')
textCorpusChristiDisplay = Show(textCorpusChristi, renderView1, 'TextSourceRepresentation')
textCorpusChristiDisplay.TextPropMode = 'Flagpole Actor'
textCorpusChristi.Text = 'Corpus Christi'
textCorpusChristiDisplay.FontSize = 45
textCorpusChristiDisplay.Bold = 1
textCorpusChristiDisplay.Shadow = 1
textCorpusChristiDisplay.BasePosition = [-97.3964, 27.8006, 0.0]
textCorpusChristiDisplay.TopPosition = [-97.3964 + viewUp[0]*viewUpScale, 27.8006 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
renderView1.Update()

textPtAransas = Text(registrationName='TextPtAransas')
textPtAransasDisplay = Show(textPtAransas, renderView1, 'TextSourceRepresentation')
textPtAransasDisplay.TextPropMode = 'Flagpole Actor'
textPtAransas.Text = 'Port Aransas'
textPtAransasDisplay.FontSize = 45
textPtAransasDisplay.Bold = 1
textPtAransasDisplay.Shadow = 1
textPtAransasDisplay.BasePosition = [-97.0611, 27.8339, 0.0]
#textPtAransasDisplay.TopPosition = [-97.0611 + viewUp[0]*viewUpScale, 27.8339 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
# Hardcoded version for temporary fix on unknown 5.9 background color issue - generalize again when issue is resolved
textPtAransasDisplay.TopPosition = [-97.0611 + viewUp[0]*viewUpScale, 27.8339 + viewUp[1]*viewUpScale, 0.0528]
renderView1.Update()

textRockport = Text(registrationName='TextRockport')
textRockportDisplay = Show(textRockport, renderView1, 'TextSourceRepresentation')
textRockportDisplay.TextPropMode = 'Flagpole Actor'
textRockport.Text = 'Rockport'
textRockportDisplay.FontSize = 45
textRockportDisplay.Bold = 1
textRockportDisplay.Shadow = 1
textRockportDisplay.BasePosition = [-97.0544, 28.0206, 0.0]
#textRockportDisplay.TopPosition = [-97.0544 + viewUp[0]*viewUpScale, 28.0206 + viewUp[1]*viewUpScale, viewUp[2]*viewUpScale]
# Hardcoded version for temporary fix on unknown 5.9 background color issue - generalize again when issue is resolved
textRockportDisplay.TopPosition = [-97.0544 + viewUp[0]*viewUpScale, 28.0206 + viewUp[1]*viewUpScale, 0.1]
renderView1.Update()

# Create a new 'Light'
light1 = AddLight(view=renderView1)
light1.Coords = 'Ambient'
light1.Intensity = 0.08
