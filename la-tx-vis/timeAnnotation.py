# Script to create a UTC time annotation based on header information from an ADCIRC netCDF file      
# Compatible with a visualization of a fort.63.nc or combined fort.63.nc and fort.74.nc.

# Requirements: before using this utility, you must use the netcdf_header_info.sh utility (found in the 
# paraview-adcirc-vis/utilities directory) to create a label_info.txt file for your netCDF file. The text
# file is processed by this Python script to create the annotation. If you are visualizing a combined
# fort.63.nc and fort.74.nc, you can create label_info.txt using either one of the files.

# Usage: when you run this script, you will be asked for input through the ParaView GUI. This input is 
# the path to the directory where the label_info.txt file which you created previously is located. 

# Note for Windows users: Make sure to include the correct prefix for the path. For example, if your 
# label_info.txt file is held in a directory called "adcirc-vis" in your C drive, then your input can
# be C:/adcirc-vis (you can also use the \\ character instead of /, but that is not necessary)

# The label created by this script has 1 line:
# Line 1: Current date/time in UTC
# The annotation is placed in the top left of the view by default.

# The time updates based on the timestep you are currently viewing.

# You should not use this script with a maxele file. If you do, there will not be an error, but there
# will be a placeholder annotation of "maxele file" which you can delete.

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Prompt user for path to directory where input netCDF file/files are
# (which by extension is where the label_info.txt file is)
dir_path = input()

renderView1 = GetActiveViewOrCreate('RenderView')

# find source
if (FindSource('fort.63.nc_fort.74.nc.xmf')) is not None:
    generalSource = FindSource('fort.63.nc_fort.74.nc.xmf')
    sourceName = 'fort.63.nc_fort.74.nc.xmf'
elif (FindSource('fort.63.nc.xmf')) is not None:
    generalSource = FindSource('fort.63.nc.xmf')
    sourceName = 'fort.63.nc.xmf'
elif (FindSource('maxele.63.nc.xmf')) is not None:
    generalSource = FindSource('maxele.63.nc.xmf')
    sourceName = 'maxele.63.nc.xmf'
	
# create a new 'Programmable Annotation'
programmableAnnotation1 = ProgrammableAnnotation(registrationName='ProgrammableAnnotation1', Input=generalSource)
programmableAnnotation1.PythonPath = ''

# Properties modified on programmableAnnotation1
programmableAnnotation1.Script = """from datetime import datetime, timedelta
from os import path
from re import findall

mydir = \"""" + dir_path + """\"

myfile = "label_info.txt"

path = path.join(mydir, myfile)

with open(path) as header_file:
    header_list = [findall(r\'\\"(.*?)\\"\',line) for line in open(path)]
	
# Setup: get date/time info in proper format to pass to calendar
datetime_string = header_list[5][0]
ymd_string = datetime_string.split(' ')[2]
hms_string = datetime_string.split(' ')[3]
year = int(ymd_string.split('-')[0])
month = int(ymd_string.split('-')[1])
day = int(ymd_string.split('-')[2])
hour = int(hms_string.split(':')[0])
min = int(hms_string.split(':')[1])
sec = int(hms_string.split(':')[2])

# Pass date/time info to calendar
date_since = datetime(year,month,day,hour,min,sec)

# Get current "seconds after" time
sec_add = inputs[0].GetInformation().Get(vtk.vtkDataObject.DATA_TIME_STEP())

date_curr = date_since + timedelta(seconds=sec_add)

source_type = \"""" + sourceName + """\"

to = self.GetTableOutput()
arr = vtk.vtkStringArray()
arr.SetName("Text")
arr.SetNumberOfComponents(1)
if source_type == "maxele.63.nc.xmf":
    arr.InsertNextValue("maxele file")
else:
    arr.InsertNextValue(str(date_curr) + ' ' + "UTC")
to.AddColumn(arr)"""

# show data in view
programmableAnnotation1Display = Show(programmableAnnotation1, renderView1, 'TextSourceRepresentation')

programmableAnnotation1Display.Bold = 1
programmableAnnotation1Display.Shadow = 1
programmableAnnotation1Display.FontSize = 21

# update the view to ensure updated data information
renderView1.Update()