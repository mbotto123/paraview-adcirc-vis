#!/bin/sh
############################################################
# Shell script to download a subset of a NetCDF file using #
# OPeNDAP with the NCO ncks utility.                       #
#                                                          #
# Intended to be used to download large files where the    #
# user does not want the data for all time values in the   #
# file. The user can choose an upper bound for the time    #
# variable as a parameter with this utility.               #
#                                                          #
# (Required) Input #1: the OPeNDAP URL to the file         #
# (Required) Input #2: upper bound for the time variable   #
# - Lower bound assumed to be 0                            #
# (Optional) Input #3: name of resulting file              #
#                                                          #
# Output: The requested NetCDF file is downloaded to the   #
# directory where this utility is executed.                #
#                                                          #
# Requirements: Installation of the NetCDF Operators       #
# (NCO) package, which includes the utility ncks.          #
#                                                          #
# Usage example:                                           #
# ./netcdf_timeslice_dap.sh <dap-url> 9 fort.63.nc         #
# - Downloads data from the given url from times 0 to 9 to #
#   a file named fort.63.nc                                #
#                                                          #
# Notes:                                                   #
# - There is no progress bar for the download              #
# - ncks utility is part of NetCDF Operators (NCO)         #
#   http://nco.sourceforge.net/                            #
############################################################

# Error handling for incorrect number of arguments
if [ "$#" -ne 2 ] && [ "$#" -ne 3 ]; then
    echo "------------------------------------------"
    echo "Incorrect number of arguments."
    echo "------------------------------------------"
    echo "Usage:"
    echo "------------------------------------------"
    echo "Argument 1: OPeNDAP URL"
    echo "Argument 2: Upper bound for time variable."
    echo "------------------------------------------"
    echo "OR:"
    echo "------------------------------------------"
    echo "Argument 1: OPeNDAP URL"
    echo "Argument 2: Upper bound for time variable"
    echo "Argument 3: Name of destination file"
    echo "------------------------------------------"
    echo "Exiting..."
    exit 1
fi

# Run the ncks utility with default destination filename corresponding to the downloaded file
# Optional 3rd argument allows for user-defined destination filename
# If a file already exists with the requested destination filename, ncks will prompt the user for a decision

# Includes basic error handling for user-input OPeNDAP URL based on the end of the URL
# If the URL is correct, this check confirms the file type

case "$1" in
    *fort.63.nc) echo "Downloading a fort.63 file..."
    if [ "$#" -eq 2 ]; then
        ncks -7 -h -L 5 -d time,0,"$2" "$1" -o fort.63.nc
    elif [ "$#" -eq 3 ]; then
        ncks -7 -h -L 5 -d time,0,"$2" "$1" -o "$3" 
    fi
    ;;
    *fort.74.nc) echo "Downloading a fort.74 file..."
    if [ "$#" -eq 2 ]; then
        ncks -7 -h -L 5 -d time,0,"$2" "$1" -o fort.74.nc 
    elif [ "$#" -eq 3 ]; then
        ncks -7 -h -L 5 -d time,0,"$2" "$1" -o "$3" 
    fi
    ;;
    # Exit if ending of file does not match supported types or is misspelled.
    # Note that if a different part of the URL than the ending is misspelled, then this utility will not catch it
    # and you will get a different error from nccopy.
    *) echo "OPeNDAP URL file type not compatible or misspelled. Exiting..."
    exit 1
    ;;
esac

# Meaning of ncks options:
# -7 means netCDF4-classic format, which is the same as what you would get if you wget an ADCIRC/ASGS NetCDF
# file from the THREDDS servers, so it is used here for consistency.
#
# -h means do not append the command used to download the file to the NetCDF header's history attribute.
#
# -L 5 means a compression level of 5, which is used to reduce the file size. If this is not used, the 
# result of a download through DAP will actually be larger in terms of storage than the same file downloaded
# through something like wget.
#
# -d performs the subsetting of the file (subset is called a "hyperslab" in NetCDF terminology) 
#
# -o specifies the destination file name
