#!/usr/bin/python

#
# tcr.cgi
#
# Does a simple Location: HTTP redirect to split between two different 
# tile caches based on the zoom level.
#

import os

# Get the URI to parse
p = os.environ['REQUEST_URI']

# Split up based on /
parts = p.split('/')
l = len(parts) - 1

# Y is last
y = parts[l]
(y, ext) = y.split('.')

# X is penultimate
l -= 1
x = parts[l]

# Zoom is third to last
l -= 1
z = parts[l]

if int(zoom) < 16:
  # TNM Vector Basemap Small Scale Cache
  tnm = 'http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile'

  print "Location:     " + tnm + "/" + zoom + "/" + y + "/" + x + ".png\r\n\r"
else:
  # TNM Vector Basemap Large Scale Local TileCache

  # Switch server names as needed
  s = os.environ['SERVER_NAME']
  
  tc = 'http://' + s + '/tiles/tilecache.cgi/1.0.0/tnm'

  print "Location:     " + tc + "/" + zoom + "/" + x + "/" + y + ".png\r\n\r"
