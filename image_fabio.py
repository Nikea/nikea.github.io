# Copyright (c) Brookhaven National Lab 2O14
# All rights reserved
# BSD License
# See LICENSE for full text
############################################################################
#
#   This module is for Read the .tiff file(load_tif) using FabIO 
#   
#   FabIO
#   =====
#   FabIO is an I/O library for images produced by 2D X-ray detectors
#   and written in python. FabIO support images detectors from a dozen
#   of companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford,.),
#   for a total of 20 different file formats (like CBF, EDF, TIFF, ...)
#   and offers an unified interface to their headers (as a python dictionary)
#   and datasets (as a numpy ndarray of integers or floats)
#   https://github.com/kif/fabio
#
##############################################################################


import os
import glob
import fabio

def datalist(dirpath):
    """
    Parameters
    ----------
    dirpath : string
    Complete path to the directory
    -----------------------------------------
    Returns
    -------
    output: image details
    reading the image data
    """
    A = glob.glob(os.path.join(dirpath, '*.tif'))
    datalist_l = len(A)
    print datalist_l
    for file in A:
        image_data, filename = load_tif(file)
    return

def load_tif(file):
    """
    Parameters
    ----------
    file_name: string
    Complete path to the file to be loaded into memory
    ----------------------------------------------------
    Returns
    -------
    output: NxN ndarray
    Returns a numpy array of the original tiff file
    """
    filename = os.path.basename(file)
    print('loading ' + filename)
    image = fabio.open(file)
    image_data = image.data
    print 'Volume loaded successfully'
    return image_data
