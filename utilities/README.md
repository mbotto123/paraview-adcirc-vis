# General Utilities

This directory holds general utilities for working with ADCIRC netCDF files.

- `netcdf_header_info.sh`: Shell script to pull specific information from the header of a NetCDF output file generated by ADCIRC through the 
ASGS and copy it to a text file which will be read by a ParaView Python script to create an annotation. See the script's comment header for more details.
    - Usage example: `netcdf_header_info.sh fort.63.nc` creates the file `label_info.txt` in the same directory as `fort.63.nc`.