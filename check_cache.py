#!/usr/bin/env python

# Walks the tile cache and reports how many files are missing

import os, sys

import TileMath
import caches

cache = sys.argv[1]
print "Checking cache for " + cache

zooms = caches.cacheZoom(cache)
print "Levels " + str(zooms[0]) + " to " + str(zooms[1])

print "BBox: " + str(caches.bbox[0]) + ", " \
               + str(caches.bbox[1]) + ", " \
               + str(caches.bbox[2]) + ", " \
               + str(caches.bbox[3])

tiles = []  
  
for zoom in range(zooms[0], zooms[1]):
    (xstart, ystart) = TileMath.WGS84toTileXY(caches.bbox[1], caches.bbox[0], zoom)
    (xend, yend) = TileMath.WGS84toTileXY(caches.bbox[3], caches.bbox[2], zoom)

    print "Zoom: " + str(zoom)
    print "Start: " + str(xstart) + ", " + str(ystart)
    print "End: " + str(xend) + ", " + str(yend)
 
    lpth = '/' + str(zoom)
    
    #if not os.path.exists(tnm_path + lpth):
    #    os.makedirs(tnm_path + lpth)
    
    for y in range(ystart, yend):
        for x in range(xstart, xend):
            xpth = lpth + '/' + str(x)
            #if not os.path.exists(tnm_path + xpth):
            #    os.makedirs(tnm_path + xpth)
        
            local = caches.tc_root + cache + '/' + str(x) + '/' + str(y) + '.png'
            #remote = tnm_url + lpth + '/' + str(y) + '/' + str(x) + '.png'

            tiles.append(local)

print "Full cache tile count: " + str(len(tiles))

      
#while len(tiles) > 0:
#  (local, remote, retries) = tiles.pop(0)
#  
#  print "Getting " + remote
#      
#  try:
#    urllib.urlretrieve(remote, local)
#  except:
#    if retries < 10:
#      retries += 1
#      tiles.append([local, remote, retries])
#    else:
#      print "Failed to get " + remote


  
