# Script to add location labels, compatbile with zoomToLaTx2D-moreLand script

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

text1 = Text()
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
text1.Text = 'Houston .'
text1Display.FontSize = 9
text1Display.Bold = 1
text1Display.Shadow = 1
text1Display.WindowLocation = 'AnyLocation'
text1Display.Position = [0.065, 0.74]
renderView1.Update()

text2 = Text()
text2Display = Show(text2, renderView1, 'TextSourceRepresentation')
text2.Text = 'Galveston .'
text2Display.FontSize = 9
text2Display.Bold = 1
text2Display.Shadow = 1
text2Display.WindowLocation = 'AnyLocation'
text2Display.Position = [0.1, 0.64]
renderView1.Update()

text3 = Text()
text3Display = Show(text3, renderView1, 'TextSourceRepresentation')
text3.Text = '. Bolivar Peninsula'
text3Display.FontSize = 6
text3Display.Bold = 1
text3Display.Shadow = 1
text3Display.WindowLocation = 'AnyLocation'
text3Display.Position = [0.22, 0.66]
renderView1.Update()

text4 = Text()
text4Display = Show(text4, renderView1, 'TextSourceRepresentation')
text4.Text = '. New Orleans'
text4Display.FontSize = 9
text4Display.Bold = 1
text4Display.Shadow = 1
text4Display.WindowLocation = 'AnyLocation'
text4Display.Position = [0.72, 0.77]
renderView1.Update()

text5 = Text()
text5Display = Show(text5, renderView1, 'TextSourceRepresentation')
text5.Text = '. Lake Pontchartrain'
text5Display.FontSize = 6
text5Display.Bold = 1
text5Display.Shadow = 1
text5Display.WindowLocation = 'AnyLocation'
text5Display.Position = [0.71, 0.82]
renderView1.Update()

text6 = Text()
text6Display = Show(text6, renderView1, 'TextSourceRepresentation')
text6.Text = '. Lake Charles'
text6Display.FontSize = 9
text6Display.Bold = 1
text6Display.Shadow = 1
text6Display.WindowLocation = 'AnyLocation'
text6Display.Position = [0.38, 0.83]
renderView1.Update()

text7 = Text()
text7Display = Show(text7, renderView1, 'TextSourceRepresentation')
text7.Text = 'Port Arthur .'
text7Display.FontSize = 8
text7Display.Bold = 1
text7Display.Shadow = 1
text7Display.WindowLocation = 'AnyLocation'
text7Display.Position = [0.21, 0.75]
renderView1.Update()



