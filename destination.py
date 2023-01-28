import random
import math
import cmath
import argparse

def rand_loc(dist=5, stdev=.5, home=(50,3)):
    home_lat = home[0]
    dist_km=random.gauss(dist, stdev)
    angle =random.uniform(0, 2*math.pi)
    change_km=cmath.rect(dist_km, angle)
    dist_lat = change_km.imag
    dist_lon = change_km.real
    change_degrees=(degLatInKm(dist_lat), degLonInKm(dist_lon, home_lat))
    return(home[0]+change_degrees[0], home[1]+change_degrees[1])

#conversion factor coords to km based on your latitude
def degLatInKm(dist, lat=55):
    #constant assuming earth is a sphere
    # a degree latitude is about 111.2km, at my latitude
    return dist/111.2

def degLonInKm(dist, lat):
    return dist/111.32*math.cos(lat)

def readhome(filename="./home.txt"):
    try:
        f = open(filename,"r")
        line = f.readline()
        f.close()
        return [float(x) for x in line.split()]
    except:
        return 0

def sethome(lat, lon, filename="./home.txt"):
    f=open(filename, "w")
    f.write(" ".join([str(x) for x in (lat, lon)]))

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('program', type=str)
    parser.add_argument('rest', nargs=argparse.REMAINDER)
    args=parser.parse_args()
    if args.program=="home":
      restargs = args.rest
      msg = 'Input your coordinates as two numbers, for example "python destination.py home 50.123 4.96"'
      if len(restargs)<2:
        print(msg)
        exit()
      if len(restargs)>2:
          print('too many arguments, ignoring "', ' '.join(restargs[2:])+'"')
          restargs=restargs[:2]
      try:
          [lat, lon]= [float(x) for x in restargs]
      except:
          print(msg)
          exit()
      sethome(lat,lon)
    elif args.program=="dest":
      restargs = args.rest
      home=readhome()
      if home==0:
          print('First set your home location by running "python destination.py home <your coordinates>" . ')
          exit()
      try:
          dist=float(restargs[0])
      except:
          print("expected distance (a number) as first argument of destination.py dest")
      if len(restargs)>1:
          try:
              stdev=float(restargs[1])
          except:
              print("expected standard deviation (a number) as second argument of destination.py dest")
              exit()
      else:
          stdev = 0.5
      if len(restargs)>2:
          print('too many arguments, ignoring "', ' '.join(restargs[2:])+'"')
      coords_  = rand_loc(dist, stdev, home)
      coords=[str(x) for x in coords_]
      link="www.openstreetmap.org/?mlat="+coords[0]+"&mlon="+coords[1]+"&zoom=12"
      print(link)
    else:
      print('usage "destination.py home <address>" or "destination dest <distance>".  Got first keyword argument '+args.program+'instead of "home" or "dest"')  
      exit()