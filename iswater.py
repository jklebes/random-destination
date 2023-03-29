from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import numpy as np
from shapely.geometry import Polygon
import folium
import geopandas as gpd

#Use overpass to query whether the point falls in water.
#and shore proximity - keep points very close to shore
def iswater(coord, shore_dist=.1):
    return False
