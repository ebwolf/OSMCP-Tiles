#!/usr/bin/env python

# combine_tc - Overlays tile from NAIP with the matching TNM tile.
#           
# 1. Build destination directory tree and list of paths for tiles
#
# For each tile:
#
# 2. Make sure NAIP & TNM tiles exist - if not, get them
# 3. Overlay TNM onto NAIP (assumes TNM is transparent)
# 4. Optimize resulting JPEG
#

import os, urllib, imghdr

# These are relative paths
naip_path = 'naip'
tnm_path = 'tnm'
combo_path =  'combo'
tnm_url = 'http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile'
blank = tnm_url + "/5/12/3.png"

min_zoom = 0
max_zoom = 10
 
       #    min        max
       #  lat    lon     lat    lon
#bbox = ( 39.5, -105.25, 40.0, -104.5 ) # Denver
#bbox = ( 37.0, -109.10, 41.2, -102.0 ) # Colorado
#bbox = ( 37.0, -109.10, 41.2,  -94.3 ) # Colorado + Kansas
bbox = ( 24.5, -125.00, 50.0,  -66.5 ) # Contiguous 48 States

from TileMath import WGS84toTileXY

tiles = []  
  
for zoom in range(min_zoom, max_zoom):
    # The indeces in bbox don't make sense.
    (xstart, ystart) = WGS84toTileXY(bbox[2], bbox[1], zoom)
    (xend, yend) = WGS84toTileXY(bbox[0], bbox[3], zoom)

    print "Zoom: " + str(zoom)
    print "Start: " + str(xstart) + ", " + str(ystart)
    print "End: " + str(xend) + ", " + str(yend)

    lpth = '/' + str(zoom)
    if not os.path.exists(combo_path + lpth):
        os.makedirs(combo_path + lpth)
    
    for x in range(xstart, xend + 1):
        xpth = lpth + '/' + str(x)
        if not os.path.exists(combo_path + xpth):
            os.makedirs(combo_path + xpth)
      
        for y in range(ystart, yend + 1):
        
            base = naip_path + lpth + '/' + str(x) + '/' + str(y) + '.jpeg'
            tlyr = tnm_path + lpth + '/' + str(x) + '/' + str(y) + '.png'
            combo = combo_path + lpth + '/' + str(x) + '/' + str(y) + '.jpeg'

            tiles.append([base, tlyr, combo, 0])
      
            if os.path.exists(tlyr) and imghdr.what(tlyr) == 'png':
                continue
            
            # TNM tile doesn't exist locally as a valid png, get it!
            if os.path.exists(tlyr):
                os.remove(tlyr)
            
            local = tnm_path + lpth + '/' + str(x) + '/' + str(y) + '.png'
            remote = tnm_url + lpth + '/' + str(y) + '/' + str(x) + '.png'
        
            print "Need to get " + remote
            try:
                urllib.urlretrieve(remote, local)
            except:
                print "Failed to retrieve " + remote + " using blank."
                urllib.urlretrieve(blank, local)
      
while len(tiles) > 0:
    (base, tlyr, combo, retries) = tiles.pop(0)

    # If NAIP doesn't exist, just convert the TNM tile to JPEG
    if os.path.exists(base):
        #cmd = "composite -quality 40 " + tlyr + \
        #   "-alpha set -virtual-pixel transparent -channel A -blur 0x0.7 -level 50,100% +channel" + \
        #   " " + base + " " + combo      
        cmd = "composite -quality 50 " + tlyr + " " + base + " " + combo      
    else:
        cmd = "convert -quality 50 " + tlyr + " " + combo
        
    #print "."
    os.system(cmd)
  
    #cmd = "jpegoptim --strip-all -m40 " + combo
    #os.system(cmd)
  
