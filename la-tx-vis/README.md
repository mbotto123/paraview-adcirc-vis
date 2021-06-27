# Visualize ADCIRC results along the Louisiana-Texas Coast
This directory contains subdirectories for specific locations or areas along the LATX coast. Each subdirectory contains 2 types of scripts:
- ``zoomTo`` script: this script should always be used before any other script. It zooms to the area of interest and sets color mapping properties for bathymetry/topography and water surface elevation. Note that the default upper bound for the water surface elevation color map range is always set to 5 meters, but it can be changed by using the ``changeZetaUpBound`` script.
- ``labels``, ``time``, ``windVec``: these scripts add more annotations to the area of interest once the zoomTo script has been applied. They can be run in any order, as they are all independent of each other.

More details about these scripts such as which files they are compatible with can be found in the Readme files for the subdirectories, as well as in comments at the top of each script. Also, each subdirectory contains a sample image showing the effects of all scripts used together.

This directory also includes general utility scripts, which can be used with any visualization:
 - The ``changeZetaUpBound`` script provides a fast way to change the upper bound for the water surface elevation color map by prompting the user for a value through the ParaView GUI. 
 - The `discretizeColorMaps` script modifies the color maps in the visualization so that they appear discrete.

**It is recommended to run these utility scripts as macros.** If you run them from ParaView's Python shell, their effects will not be visible until after you close the shell.
