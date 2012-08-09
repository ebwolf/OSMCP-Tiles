#!/usr/bin/env python

#
# mirror_tnm.py
#
#   Kludgey mechanism to make a local copy of a remote tilecache.
#
#   In this case, I was trying to copy The National Map Small Scale Vector Basemap cache.
#

import os, sys, urllib, imghdr

tnm_path = '/osmcp/rails/public/tiles/tnm'
tnm_url = 'http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile'

from TileMath import WGS84toTileXY
  
tiles = []  

# Defaults  
#for zoom in range(0,16):

for zoom in range(15,16):
  if zoom < 8:
    # Whole world
    (xend, yend) = WGS84toTileXY(-89.9, -179.9, zoom)
    (xstart, ystart) = WGS84toTileXY(89.9, 179.9, zoom)
  elif zoom > 8 and zoom <= 12:
    # Contig US
    (xend, yend) = WGS84toTileXY(24, -125, zoom)
    (xstart, ystart) = WGS84toTileXY(50, -66, zoom)
  else:
    # Colorado
    #(xend, yend) = WGS84toTileXY(37, -102, zoom)
    (xend, yend) = WGS84toTileXY(37, -105.3, zoom)
    (xstart, ystart) = WGS84toTileXY(41, -109.6, zoom)

  print "Zoom: " + str(zoom)
  print "Start: " + str(xstart) + ", " + str(ystart)
  print "End: " + str(xend) + ", " + str(yend)
  

  lpth = '/' + str(zoom)
  if not os.path.exists(tnm_path + lpth):
    os.makedirs(tnm_path + lpth)
    
  for x in range(xstart,xend):
    xpth = lpth + '/' + str(x)
    if not os.path.exists(tnm_path + xpth):
      os.makedirs(tnm_path + xpth)
        
    for y in range(ystart,yend):
      local = tnm_path + lpth + '/' + str(x) + '/' + str(y) + '.png'
      remote = tnm_url + lpth + '/' + str(y) + '/' + str(x) + '.png'

      tiles.append([local, remote, 0])
      
while len(tiles) > 0:
  (local, remote, retries) = tiles.pop(0)
      
  try:
    if imghdr.what(local) == 'png':
      #print "Already exists..." + local
      continue
  except:
      hi = 1
    
  try:
    #print "Getting " + local
    urllib.urlretrieve(remote, local)
    #cmd = "wget " + remote + " -O " + local
    #print cmd
    #os.system(cmd)
    
    if imghdr.what(local) != 'png':
      print "Got garbage... retrying..."
      os.remove(local)
      retries += 1
      tiles.append([local, remote, retries])
    
  except Exception, err:
    print 'ERROR ' + str(err)
  
    if retries < 10:
      retries += 1
      tiles.append([local, remote, retries])
    else:
      print "Failed to get " + remote
