#!/usr/bin/python

#
# tcr.cgi
#
# Does a simple Location: HTTP redirect to split between two different 
# tile caches based on the zoom level.
#

import sys, os, imghdr, time

start = time.time()


# Switch server names as needed
s = os.environ['SERVER_NAME']

r = '/tiles/tnm'

# Get the URI to parse
p = os.environ['REQUEST_URI']

# Split up based on /
parts = p.split('/')
l = len(parts) - 1

# Y is last
try:
  y = parts[l].split('.')[0]
except:
  y = parts[l]

# X is penultimate
l -= 1
x = parts[l]

# Zoom is third to last
l -= 1
z = parts[l]

if int(z) < 16:
  # TNM Vector Basemap Small Scale Cache
  tnm = 'http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile'

  loc = tnm + "/" + z + "/" + y + "/" + x + ".png" 
  
  print "Location:     " + loc + "\r\n\r"
  elapsed = "%0.03f"%(time.time() - start)
  loc = elapsed + ' TNM: ' + loc + '\n'
  sys.stderr.write(loc)
  sys.exit(0)

# TNM Vector Basemap Large Scale Local TileCache
tc = r + '/' + z + '/' + x + '/' + y + '.png'

tc8 = tc + '8'  
if os.path.exists(tc8):
  os.rename(tc8, tc);

if os.path.exists(tc):
  loc = "http://" + s + tc
  print "Location:     " + loc + '\r\n\r'

  elapsed = "%0.03f"%(time.time() - start)
  loc = elapsed + ' HIT: ' + loc + '\n'
  sys.stderr.write(loc)
  sys.exit(0)

  
# Some portion of the path/file doesn't exist
tc = r + '/' + z
if not os.path.exists(tc):
  os.makedirs(tc)

tc = tc + '/' + x
if not os.path.exists(tc):
  os.makedirs(tc)

url = 'http://services.nationalmap.gov/ArcGIS/rest/services/transportation/MapServer/export?bboxSR=3857&size=256%2C256&format=png&transparent=true&f=image&imageSR=3857&'
#url = 'http://services.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Large/MapServer/export?bboxSR=3857&size=256%2C256&format=png&transparent=true&f=image&imageSR=3857&'
#url += 'layers=exclude:25,26,31,56,57&'
url += 'bbox='
  
# bbox=-11220955.751%2C5915002.99496%2C-11220344.2548%2C5915614.49119

import TileMath

(a,b,c,d) = TileMath.TileXYZtoGoogle(int(x),int(y),int(z))
  
bbox = str(a) + '%2C' + str(b) + '%2C' + str(c) + '%2C' + str(d)
  
src = url + bbox
dst = r + '/' + z + '/' + x + '/' + y + '.png'

import urllib
urllib.urlretrieve(src, dst)
  
loc = 'http://' + s + dst

print "Location:     " + loc + "\r\n\r"


elapsed = "%0.03f"%(time.time() - start)
loc = elapsed + ' MISS: ' + loc + '\n'
sys.stderr.write(loc)
sys.exit(0)