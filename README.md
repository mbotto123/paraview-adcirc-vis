# paraview-adcirc-vis
Python code to help with visualization of ADCIRC results using ParaView. This code automates actions such as zooming in to a specific area of interest, setting location labels, and adding wind vectors to a 2D visualization.

## Summary of contents
- Directories with names ending in ``-vis``: Contain Python scripts for different regions of interest in the US (as of June 2021, there is only one directory for regions on the Louisiana-Texas coast)
- ``color-maps``: Custom color maps that need to be loaded into ParaView. You only need to import these color maps once; afterwards, ParaView 
should automatically remember them.
- ``examples``: Example cases with instructions that can be used to reproduce a sample image.
- ``utilities``: General utilities for working with ADCIRC netCDF files.
- This Readme file contains general instructions to load ADCIRC netCDF output files into ParaView. Each ``-vis`` directory has Readme files with more specific instructions about the 
Python scripts.

## Getting Started
### First steps
- Download ParaView (version 5.8.0 or later)
- (Optional) Change the background color in ParaView. The default background color has a bluish tint so it may not provide enough contrast for visualizations that use large amounts of blue. To change the background color, select the ``Load a color palette`` button in the toolbar, select ``Edit Current Palette ...`` from the drop-down menu, scroll down to the ``Background`` section, and click on ``Background``. You can now specify RGB values. Use 107 for all three for a more neutral gray color.

The ``Load a color palette`` button looks like this: ![](./color_palette_icon.png)

### Creating an XDMF file for ADCIRC's NetCDF output
ADCIRC's netCDF output files are not readable by ParaView and need an accompanying XDMF file. The utility for generating this XDMF file is available in the ASGS repository (link to the repository: https://github.com/StormSurgeLive/asgs) in the `asgs/output` directory. Once you have cloned the ASGS repository, in the `asgs/output` directory run a modified version of this command with additional options specific to the machine you are using: 
```
make generateXDMF NETCDF=enable NETCDF4=enable NETCDF4_COMPRESSION=enable
```
By default, the makefile looks in `/usr` for a netCDF installation. If you have netCDF installed locally in `/usr`, and you have `gfortran` installed, the following version of the make command should work:
```
make generateXDMF compiler=gfortran NETCDF=enable NETCDF4=enable NETCDF4_COMPRESSION=enable
```
Otherwise, you can add the path to your netCDF installation manually to the makefile. The makefile also includes support for compiling at some HPC centers.

You will now have the executable ``generateXDMF.x`` in `asgs/output`. There is one important requirement of the netCDF files to be used with ``generateXDMF.x``: **your ADCIRC output files must be in netCDF4 format**. You can generate netCDF4 output by setting the ``NOUTGE``, ``NOUTGV``, and ``NOUTGW`` parameters to -5 or 5 in the ``fort.15`` file.  

The following line is an example of how to use ``generateXDMF.x``:
```
generateXDMF.x --datafile maxele.63.nc
```
This generates a file named ``maxele.63.nc.xmf``. You can also combine different output files:
```
generateXDMF.x --datafile fort.63.nc --datafile fort.64.nc
```
## First Visualization
### Importing color maps into ParaView
- Make sure the XDMF file you want to load and the netCDF output file/files that it depends on are in the same directory. Load the XDMF file with ParaView by using `File->Open`, select the `XDMF Reader` option when prompted, and click the `Apply` button in the `Properties` tab.
- Now you can load the color maps that are in the `color-maps` directory of this repository. To do this, scroll to the ``Display`` section of the ``Properties`` tab, and under ``Coloring`` select the ``Choose preset`` button. In this pop-up window, use the ``Import`` button to load each color map. This step is just to load the color maps so that they are stored in ParaView; the Python scripts will select the correct color map for the corresponding property.
- You only have to do this import step once. Once you close the session where you imported the color maps, then the next times you use ParaView, it should remember the files that you imported.

The ``Choose preset`` button looks like this: ![](./choose_preset_icon.png)

### Running Python scripts from ParaView's GUI
#### Option 1 : ParaView's built-in Python Shell
To run a Python script, first select `View->Python Shell`. Then, click on the Python shell so that it loads the necessary information to run scripts (you should see the line ``from paraview.simple import *`` appear in the shell). You can now use the ``Run Script`` button and select a script from this repository. Refer to the instructions in each directory's Readme file, as some scripts must be run in a certain order. Make sure to close the Python shell after running the scripts, since having it open changes the proportions of visualization elements such as color bars and labels.
#### Option 2 : Macros 
You can also run Python scripts without using the built-in shell by loading them as macros. Select `Macros->'Import new macro...'` (`Add new macro` before ParaView 5.9) and choose a script. The name of the script will now appear at the top right of the ParaView toolbar, and you can run the script by clicking on its name. ParaView will remember macros between sessions so you only need to load it once; however, if you make any changes to the script, you will need to delete the macro and load it again.
