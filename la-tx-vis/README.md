# Visualize ADCIRC results along the Louisiana-Texas Coast
This directory contains subdirectories for specific locations or areas along the LATX coast. Each subdirectory contains 2 types of scripts:
- ``zoomTo`` script: this script should always be used before any other script. It zooms to the area of interest and sets color mapping properties for bathymetry/topography and water surface elevation
- ``labels``, ``time``, ``windVec``: these scripts add more annotations to the area of interest once the zoomTo script has been applied. These scripts can be run in any order, as they are all independent of each other.

More details about these scripts such as which files they are compatible with can be found in the readme files for the subdirectories, as well as in comments at the top of each script. Also, each subdirectory contains a sample image showing the effects of all scripts used together.

Other than the subdirectories, this directory also includes the ``changeZetaUpBound`` script, which can be used with any visualization. It provides a fast way to change the upper bound for the water surface elevation color map by prompting the user for a value through the ParaView GUI.
