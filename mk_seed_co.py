#!/usr/bin/env python

#
#  mk_seed_co.py
#
#  Generates a shell script to divide a tile cache seeding operation
#  into multiple separate tasks. Also happens to be a good way to
#  stress test a WMS!
#

import os, sys, imghdr

import TileMath

layers = ['drg', 'naip', 'drg', 'idx', 'tnm']

(xend,   yend)   = TileMath.WGS84toGoogle(-105.3, 37)
(xstart, ystart) = TileMath.WGS84toGoogle(-109.6, 41)

yr = yend - ystart
xr = xend - xstart

# step^2 is the number of separate processes to divide the seeding into
step = 8

ys = yr / step
xs = xr / step

print "#!/bin/bash -x"

for y in range(0,step):
    for x in range(0,step):
        x1 = xstart + xs * x
        x2 = xstart + xs * (x + 1)  
        y1 = ystart + ys * y
        y2 = ystart + ys * (y + 1)  
        bbox = "--bbox="+str(x1)+","+str(y2)+","+str(x2)+","+str(y1)
        
        print "nohup python tilecache_seed.py " + bbox + " tnm 16 19 &"
    