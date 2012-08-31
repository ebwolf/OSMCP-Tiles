#!/usr/bin/python

import os, sys, urllib2
from TileMath import WGS84toTileXY

for zoom in range(5,20):
  if zoom < 8:
    xstart = 0
    ystart = 0
    xend = 2 ** zoom
    yend = 2 ** zoom
    # Whole world
    #(xend, yend) = WGS84toTileXY(-89, 179, zoom)
    #(xstart, ystart) = WGS84toTileXY(89, -179, zoom)
  elif zoom > 8 and zoom <= 12:
    # Contig US
    (xend, yend) = WGS84toTileXY(23, -125, zoom)
    (xstart, ystart) = WGS84toTileXY(50, -66, zoom)
  else:
    # Colorado
    #(xend, yend) = WGS84toTileXY(37, -102, zoom)
    (xend, yend) = WGS84toTileXY(36, -105, zoom)
    (xstart, ystart) = WGS84toTileXY(42, -110, zoom)

  print "Zoom: " + str(zoom)
  print "Start: " + str(xstart) + ", " + str(ystart)
  print "End: " + str(xend) + ", " + str(yend)

  for x in range(xstart, xend + 1):
    for y in range(ystart, yend + 1):
      url = 'http://navigator.er.usgs.gov/tiles/ccr.cgi/' + str(zoom) + '/' + str(x) + '/' + str(y)

      print "Get " + url      
      try:
        urllib2.urlopen(url)
      except:
        whatever = 1
        
