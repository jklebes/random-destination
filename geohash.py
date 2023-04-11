import hashlib, datetime, struct, sys, re
from urllib.request import urlopen
from urllib.error import HTTPError
import numpy as np


def geohash(home):
    # code from https://geohashing.site/geohashing/Implementations/Libraries/Python
    myLat=int(home[0])
    myLon=int(home[1])
    if myLon < -30:
        td30 = 0
    else:
        td30 = 1
    if myLat < 0:
        south = -1
    else:
        south = 1
    if myLon < 0:
        west = -1
    else:
        west = 1
    date = datetime.date.today()
    try:
        djia = urlopen((date - datetime.timedelta(td30)).strftime("http://carabiner.peeron.com/xkcd/map/data/%Y/%m/%d")).read().decode('utf-8')
    except HTTPError:
        sys.exit(sys.stderr.write('Dow Jones not available yet.\n'))
    sum_ = hashlib.md5(bytes('{0}-{1}'.format(date,djia), 'utf-8')).digest()
    n, w = [d*(abs(a)+f) for d, f, a in zip((south, west),
    [x/2.**64 for x in struct.unpack_from(">QQ", sum_)], [myLat, myLon])]
    return (n,w)

def closest_geohash(home):
    coords=[]
    dist_sq=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            coord = geohash((home[0]+i,home[1]+j))
            if not iswater(coord)
                coords.append(coord)
                dist_sq.append((home[0]-coord[0])**2 + (home[1]-coord[1])**2)
    if len(coords)>0:
        min_index = np.argmin(dist_sq)
        return coords[min_index]
    else:
        print("No land geohashes near your location today!")
        return None
