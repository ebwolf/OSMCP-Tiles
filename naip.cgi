#!/usr/bin/python

#
# tcr.cgi
#
# Does a simple Location: HTTP redirect to split between two different 
# tile caches based on the zoom level.
#

import os, sys

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

if int(z) < 12:
  # NAIP Small Scale Imagery Cache
  naip = 'http://raster1.nationalmap.gov/ArcGIS/rest/services/TNM_Small_Scale_Imagery/MapServer/tile'

  loc = naip + "/" + z + "/" + y + "/" + x
else:
  # TNM Vector Basemap Large Scale Local TileCache

  # Switch server names as needed
  s = os.environ['SERVER_NAME']
  
  tc = 'http://' + s + '/tiles/tilecache.cgi/1.0.0/naip'

  loc = tc + "/" + z + "/" + x + "/" + y

print "Location:     " + loc + "\r\n\r"
loc = 'NAIP: ' + loc + '\n'
sys.stderr.write(loc)
