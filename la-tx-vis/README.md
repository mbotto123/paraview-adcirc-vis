# Visualize ADCIRC results along the Louisiana-Texas Coast
## Subdirectories
This directory contains subdirectories for specific areas along the LA-TX coast. Each subdirectory contains 2 types of scripts:
- ``zoomTo`` script: this script should always be used before any other script. It zooms to the area of interest and sets color mapping properties for bathymetry/topography and water surface elevation. Note that the default upper bound for the water surface elevation color map range is always set to 5 meters, but it can be changed by using the ``changeZetaUpBound`` script.
- ``labels``, ``relTime``, ``windVec``: these scripts add more annotations to the area of interest once the zoomTo script has been applied. They can be run in any order, as they are all independent of each other.

More details about these scripts such as which files they are compatible with can be found in the Readme files for the subdirectories, as well as in comments at the top of each script. Also, each subdirectory contains a sample image showing the effects of all scripts used together.

## General utility scripts
This directory also includes general utility scripts, which can be used with any visualization:
- The ``changeZetaUpBound`` script provides a fast way to change the upper bound for the water surface elevation color map by prompting the user for a value through the ParaView GUI. 
- The `discretizeColorMaps` script modifies the color maps in the visualization so that they appear discrete. You can undo its effects with `unDiscretizeColorMaps`.

**It is recommended to run these utility scripts as macros.** If you run them from ParaView's Python shell, their effects will not be visible until after you close the shell.

## Annotation utility scripts
`fullAnnotation` and `timeAnnotation` provide more descriptive annotations and are mostly compatible with any visualization; however, `timeAnnotation` should not be used with `maxele` files.
The following bullet points summarize what each does:
- `timeAnnotation` creates a date/time annotation in UTC (formatted YYYY-MM-DD HH:MM:SS) placed in the top-left corner of the visualization.
- `fullAnnotation` creates the same date/time annotation and also adds more information such as the model and grid name, and storm/advisory information.

In both cases, the time updates automatically as you cycle through different time steps in the visualization, so these annotations can be used for animations as well as still images. **These scripts 
expect that the header of your netCDF file is formatted according to ASGS standards.** If the header format is significantly different, then the annotations may not work as expected.

Both scripts need information from the header of the netCDF file used for visualization, so there are two required steps before using them:
1. First, run the `netcdf_header_info.sh` utility - found in the `paraview-adcirc-vis/utilities` directory - on the netCDF file you want to visualize. If your visualization uses more than one netCDF file,
you only need to run the utility on one of them. Note that this utility requires you to have a netCDF installation, with the `ncdump` utility on your path.
2. The utility creates a file called `label_info.txt`. Copy the full path to the **directory** where this file is located (not including the file name); the `fullAnnotation` and `timeAnnotation` scripts will prompt you to enter this
path through the ParaView GUI. For Windows users, see the header comments of these scripts for path formatting rules.

For convenience, it is also recommended to run these scripts as macros.
