import random
import math

#get random point and open
def generate_link(home, distance=5, error=.3):
    angle = random.uniform(0, math.pi*2)
    distance = random.gauss(distance, error)
    dist_lat = distance * math.sin(angle)
    dist_lon = distance * math.cos(angle)
    (lat, lon) = home
    coord_out = (lon+convert_lon(dist_lon, lon),
      lat+convert_lat(dist_lat, lat))
    print("https://www.openstreetmap.org/?mlat="+str(lat)+
        "&mlon="+str(lon)+"&zoom=12")

#conversion factor coords to km based on your latitude
def convert_lat(dist, lat):
    #constant assuming earth is a sphere
    # a degree latitude is about 111.2km, at my latitude
    return dist/111.2

def convert_lon(dist, lat):
    return dist/111.32*math.cos(lat)

#query location 
#resolve - file, address, or coords

#main script - TODO wrap in command line tool
if __name__=="__main__":
    home = (46.65,14.86)
    generate_link(home, distance=5, error=.3)