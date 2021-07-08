# Script to add location labels, compatible with zoomToLATX2D-LL script

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

## Houston
textHouston = Text(registrationName='TextHouston')
textHoustonDisplay = Show(textHouston, renderView1, 'TextSourceRepresentation')
textHoustonDisplay.TextPropMode = 'Billboard 3D Text'
textHouston.Text = 'Houston '
textHoustonDisplay.FontSize = 30
textHoustonDisplay.Bold = 1
textHoustonDisplay.Shadow = 1
textHoustonDisplay.Justification = 'Right'
textHoustonDisplay.BillboardPosition = [-95.3698, 29.7604, 0.05]

pinHouston = Sphere(registrationName='PinHouston')
pinHouston.Center = [-95.3698, 29.7604, 0.0]
pinHouston.Radius = 0.025
pinHoustonDisplay = Show(pinHouston, renderView1, 'GeometryRepresentation')

## Galveston
textGalveston = Text(registrationName='TextGalveston')
textGalvestonDisplay = Show(textGalveston, renderView1, 'TextSourceRepresentation')
textGalvestonDisplay.TextPropMode = 'Billboard 3D Text'
textGalveston.Text = 'Galveston '
textGalvestonDisplay.FontSize = 30
textGalvestonDisplay.Bold = 1
textGalvestonDisplay.Shadow = 1
textGalvestonDisplay.Justification = 'Right'
textGalvestonDisplay.BillboardPosition = [-94.7977, 29.3013, 0.05]

pinGalveston = Sphere(registrationName='PinGalveston')
pinGalveston.Center = [-94.7977, 29.3013, 0.0]
pinGalveston.Radius = 0.025
pinGalvestonDisplay = Show(pinGalveston, renderView1, 'GeometryRepresentation')

## Bolivar Peninsula
textBolivarP = Text(registrationName='TextBolivarP')
textBolivarPDisplay = Show(textBolivarP, renderView1, 'TextSourceRepresentation')
textBolivarPDisplay.TextPropMode = 'Billboard 3D Text'
textBolivarP.Text = ' Bolivar Peninsula'
textBolivarPDisplay.FontSize = 25
textBolivarPDisplay.Bold = 1
textBolivarPDisplay.Shadow = 1
textBolivarPDisplay.Justification = 'Left'
textBolivarPDisplay.BillboardPosition = [-94.5799, 29.4783, 0.05]

pinBolivarP = Sphere(registrationName='PinBolivarP')
pinBolivarP.Center = [-94.5799, 29.4783, 0.0]
pinBolivarP.Radius = 0.025
pinBolivarPDisplay = Show(pinBolivarP, renderView1, 'GeometryRepresentation')

## New Orleans
textNewOrleans = Text(registrationName='TextNewOrleans')
textNewOrleansDisplay = Show(textNewOrleans, renderView1, 'TextSourceRepresentation')
textNewOrleansDisplay.TextPropMode = 'Billboard 3D Text'
textNewOrleans.Text = ' New Orleans'
textNewOrleansDisplay.FontSize = 30
textNewOrleansDisplay.Bold = 1
textNewOrleansDisplay.Shadow = 1
textNewOrleansDisplay.Justification = 'Left'
textNewOrleansDisplay.BillboardPosition = [-90.0715, 29.9511, 0.05]

pinNewOrleans = Sphere(registrationName='PinNewOrleans')
pinNewOrleans.Center = [-90.0715, 29.9511, 0.0]
pinNewOrleans.Radius = 0.025
pinNewOrleansDisplay = Show(pinNewOrleans, renderView1, 'GeometryRepresentation')

## Lake Pontchartrain
textPontchartrain = Text(registrationName='TextPontchartrain')
textPontchartrainDisplay = Show(textPontchartrain, renderView1, 'TextSourceRepresentation')
textPontchartrainDisplay.TextPropMode = 'Billboard 3D Text'
textPontchartrain.Text = ' Lake Pontchartrain'
textPontchartrainDisplay.FontSize = 25
textPontchartrainDisplay.Bold = 1
textPontchartrainDisplay.Shadow = 1
textPontchartrainDisplay.Justification = 'Left'
textPontchartrainDisplay.BillboardPosition = [-90.1121, 30.2051, 0.05]

pinPontchartrain = Sphere(registrationName='PinPontchartrain')
pinPontchartrain.Center = [-90.1121, 30.2051, 0.0]
pinPontchartrain.Radius = 0.025
pinPontchartrainDisplay = Show(pinPontchartrain, renderView1, 'GeometryRepresentation')

## Update render view with all changes at once
renderView1.Update()
