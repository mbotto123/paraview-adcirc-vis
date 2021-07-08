# This script makes a time annotation for a 3D view that includes areas around Corpus Christi and Port Aransas
# Time is expressed relative to the starting time of the simulation

# Can handle a ParaView visualization made from following ADCIRC output files: 
# fort.63.nc, or combined fort.63.nc and fort.74.nc

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')

# find source
if (FindSource('fort.63.nc_fort.74.nc.xmf')) is not None:
	generalSource = FindSource('fort.63.nc_fort.74.nc.xmf')
elif (FindSource('fort.63.nc.xmf')) is not None:
	generalSource = FindSource('fort.63.nc.xmf')

# Create filter to find the initial time of the simulation
extractTimeSteps1 = ExtractTimeSteps(Input=generalSource)
extractTimeSteps1.SelectionMode = 'Select Time Range'
extractTimeSteps1.TimeStepRange = [0, 0]
timeInit = extractTimeSteps1.TimestepValues

# destroy extractTimeSteps1
Delete(extractTimeSteps1)
del extractTimeSteps1

# create a new 'Annotate Time Filter' 
relTimeAnnotation = AnnotateTimeFilter(registrationName='RelativeTimeAnnotation',Input=generalSource)

# annotate time in hours relative to the initial timestep
relTimeAnnotation.Format = 'Time: +%.1f hours'
relTimeAnnotation.Scale = 2.777777778e-04
# shift annotated time back by initial time so that it starts at zero 
relTimeAnnotation.Shift = -1.0*relTimeAnnotation.Scale*timeInit

# show data in view
relTimeAnnotationDisplay = Show(relTimeAnnotation, renderView1, 'TextSourceRepresentation')

# font size change (needs to happen after Show() )
relTimeAnnotationDisplay.FontSize = 30


