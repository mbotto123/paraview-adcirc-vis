# paraview-adcirc-vis
Python code to help with visualization of ADCIRC results using ParaView. Each directory corresponds to a different region of interest. 

First steps:
- Download ParaView. Using version 5.8 will ensure you can run all of the scripts. Some scripts will not work on previous versions; for example, location labels will not work on any versions before 5.8.
- (Optional) Change the background color in ParaView. The default background color has a bluish tint so it may not provide enough contrast for visualizations that use large amounts of blue. To change the background color, select the 'Load a color palette' button in the toolbar, select 'Edit Current Palette ...' from the drop-down menu, scroll down to the 'Background' section, and click on Background. You can now specify RGB values. Use 107 for all three for a more neutral gray color.

Creating an XML file for ADCIRC's netcdf output:
ADCIRC's netcdf output files are not readable by ParaView and need an accompanying XML file. The utility for generating this XML file is available in the ASGS repository (link to the repository: https://github.com/jasonfleming/asgs) in the output directory. You will need to clone the ASGS repository and in the output directory run this command, although you will also need to add compiler options specific to the machine you are using: 
```
make all NETCDF=enable NETCDF4=enable NETCDF4_COMPRESSION=enable. 
```
For example, on Lonestar5 at TACC, the command will be: 
```
make all compiler=intel MACHINENAME=lonestar NETCDF=enable NETCDF4=enable NETCDF4_COMPRESSION=enable
```


