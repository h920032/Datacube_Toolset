import os,sys
import datetime
import datacube
import xarray as xr
import pandas as pd
import numpy as np

def ndvi_point(dataset, base_lat, base_lon, cloud_free_index):
    pixel_coordinates = {"latitude":base_lat,"longitude": base_lon}
    pixel = landsat.sel(**pixel_coordinates, method = 'nearest')
    point = pixel.where(pixel.pixel_qa == cloud_free_index)
    ndvi = (point.nir - point.red)/(point.nir + point.red)
    result = pd.DataFrame({'time':ndvi.time.values})
    result['ndvi'] = ndvi.values
    result = result[~result['ndvi'].isin(['NaN'])]
    return result