#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trickbox
A module that contains a box of useful frunctions.

Created on Sat Jan 26 14:37:05 2019

@author: tammas
"""

import numpy as np
import scipy.interpolate as interp


def regrid_maps(oldlat,oldlon,data,newlat,newlon,method='cubic'):
    """regrid_3d interpolates a series of maps to a new grid.
    Arguments:
        oldlat - ndarray of old latittudes (j)
        oldlon - ndarray of old longitudes (j)
        data - ndarray of data with shape (n,j,i)
        newlat - ndarray of new latitudes (A)
        newlon - ndarray of new longitudes (B)
    Returns:
        regrided - regrided data (n,A,B)
    """
    X, Y = np.meshgrid(oldlon, oldlat)
    XX, YY = np.meshgrid(newlon, newlat)
    regrided = np.empty((data.shape[0],newlat.size,newlon.size))
    for n in range(data.shape[0]):
        regrided[n,...] = interp.griddata((X.flatten(),Y.flatten()),
                data[n].flatten(),
                (XX,YY),
                method=method)
    return regrided

if __name__=='__main__':
    #old grid dim
    loni = np.arange(-180,181,10)
    lati = np.arange(-90,91,10)
    old_data = np.random.rand(20,lati.size,loni.size)
    #new grid dim
    lon = np.arange(-180,181,3)
    lat = np.arange(-90,91,3)
    
    new_data = regrid_maps(lati,loni,old_data,lat,lon)