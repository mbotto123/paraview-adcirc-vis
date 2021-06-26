# Script to add location labels, compatible with zoomToLATX2D-ML script

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

## Houston
text1 = Text()
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
text1Display.TextPropMode = 'Billboard 3D Text'
text1.Text = 'Houston '
text1Display.FontSize = 30
text1Display.Bold = 1
text1Display.Shadow = 1
text1Display.Justification = 'Right'
text1Display.BillboardPosition = [-95.3698, 29.7604, 0.05]

sphere1 = Sphere()
sphere1.Center = [-95.3698, 29.7604, 0.0]
sphere1.Radius = 0.025
sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

## Galveston
text2 = Text()
text2Display = Show(text2, renderView1, 'TextSourceRepresentation')
text2Display.TextPropMode = 'Billboard 3D Text'
text2.Text = 'Galveston '
text2Display.FontSize = 30
text2Display.Bold = 1
text2Display.Shadow = 1
text2Display.Justification = 'Right'
text2Display.BillboardPosition = [-94.7977, 29.3013, 0.05]

sphere2 = Sphere()
sphere2.Center = [-94.7977, 29.3013, 0.0]
sphere2.Radius = 0.025
sphere2Display = Show(sphere2, renderView1, 'GeometryRepresentation')

## Bolivar Peninsula
text3 = Text()
text3Display = Show(text3, renderView1, 'TextSourceRepresentation')
text3Display.TextPropMode = 'Billboard 3D Text'
text3.Text = ' Bolivar Peninsula'
text3Display.FontSize = 25
text3Display.Bold = 1
text3Display.Shadow = 1
text3Display.Justification = 'Left'
text3Display.BillboardPosition = [-94.5799, 29.4783, 0.05]

sphere3 = Sphere()
sphere3.Center = [-94.5799, 29.4783, 0.0]
sphere3.Radius = 0.025
sphere3Display = Show(sphere3, renderView1, 'GeometryRepresentation')

## New Orleans
text4 = Text()
text4Display = Show(text4, renderView1, 'TextSourceRepresentation')
text4Display.TextPropMode = 'Billboard 3D Text'
text4.Text = ' New Orleans'
text4Display.FontSize = 30
text4Display.Bold = 1
text4Display.Shadow = 1
text4Display.Justification = 'Left'
text4Display.BillboardPosition = [-90.0715, 29.9511, 0.05]

sphere4 = Sphere()
sphere4.Center = [-90.0715, 29.9511, 0.0]
sphere4.Radius = 0.025
sphere4Display = Show(sphere4, renderView1, 'GeometryRepresentation')

## Lake Pontchartrain
text5 = Text()
text5Display = Show(text5, renderView1, 'TextSourceRepresentation')
text5Display.TextPropMode = 'Billboard 3D Text'
text5.Text = ' Lake Pontchartrain'
text5Display.FontSize = 25
text5Display.Bold = 1
text5Display.Shadow = 1
text5Display.Justification = 'Left'
text5Display.BillboardPosition = [-90.1121, 30.2051, 0.05]

sphere5 = Sphere()
sphere5.Center = [-90.1121, 30.2051, 0.0]
sphere5.Radius = 0.025
sphere5Display = Show(sphere5, renderView1, 'GeometryRepresentation')

## Lake Charles
text6 = Text()
text6Display = Show(text6, renderView1, 'TextSourceRepresentation')
text6Display.TextPropMode = 'Billboard 3D Text'
text6.Text = ' Lake Charles'
text6Display.FontSize = 30
text6Display.Bold = 1
text6Display.Shadow = 1
text6Display.Justification = 'Left'
text6Display.BillboardPosition = [-93.2174, 30.2266, 0.0]

sphere6 = Sphere()
sphere6.Center = [-93.2174, 30.2266, 0.0]
sphere6.Radius = 0.025
sphere6Display = Show(sphere6, renderView1, 'GeometryRepresentation')

## Port Arthur
text7 = Text()
text7Display = Show(text7, renderView1, 'TextSourceRepresentation')
text7Display.TextPropMode = 'Billboard 3D Text'
text7.Text = 'Port Arthur '
text7Display.FontSize = 28
text7Display.Bold = 1
text7Display.Shadow = 1
text7Display.Justification = 'Right'
text7Display.BillboardPosition = [-93.9399, 29.8850, 0.0]

sphere7 = Sphere()
sphere7.Center = [-93.9399, 29.8850, 0.0]
sphere7.Radius = 0.025
sphere7Display = Show(sphere7, renderView1, 'GeometryRepresentation')

## Update render view with all changes at once
renderView1.Update()