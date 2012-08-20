#!/usr/bin/python

#
# ccr.cgi
#
# Combines NAIP and TNM into a single tile
#
import sys, os

# Switch server names as needed
s = os.environ['SERVER_NAME']

r = '/tiles/combo'

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


# Large scales redirect to NAIP
if int(z) > 15:
  tc = 'http://' + s + '/tiles/tilecache.cgi/1.0.0/naip/' + z + '/' + x + '/' + y + '.jpeg'

  loc = "Location:     " + tc + "\r\n\r"
  
  print loc
  
  loc = 'NAIP: ' + loc + '\n'
  sys.stderr.write(loc) 
  
  sys.exit(0)
 

# Do we already have this combo tile?
fp = r + '/' + z + '/' + x + '/' + y + '.jpeg'

#import imghdr
if os.path.exists(fp): # imghdr.what(fp) == 'jpeg':
  tc = 'http://' + s + fp

  loc = "Location:     " + fp + "\r\n\r"
  
  print loc
  
  loc = 'COMBO HIT: ' + loc
  sys.stderr.write(loc) 
  sys.exit(0)
else:
  poop = "MISS: " + fp + '\n'
  sys.stderr.write(poop)


# Get the TNM tile from TCR.CGI - tcr takes z-x-y
tnm = 'http://' + s + '/tiles/tcr.cgi' + "/" + z + "/" + x + "/" + y + ".png"

# Get the NAIP tile from NAIP.CGI
#naip = 'http://' + s + '/tiles/tilecache.cgi/1.0.0/naip' + "/" + z + "/" + x + "/" + y + ".jpeg"
naip = 'http://' + s + '/tiles/naip.cgi' + "/" + z + "/" + x + "/" + y + ".jpeg"

from PIL import Image, ImageEnhance
import cStringIO
import urllib2

tnmrsp = urllib2.urlopen(tnm)
tnm_im = Image.open(cStringIO.StringIO(tnmrsp.read()))

naiprsp = urllib2.urlopen(naip)
naip_im = Image.open(cStringIO.StringIO(naiprsp.read()))


# Make a greyscale image to blend with
gs = Image.new('RGB', (256,256), (128,128,128))

im = Image.blend(naip_im, gs, .4)
#en = ImageEnhance.Brightness(naip_im)
#im = en.enhance(1.5)
im.paste(tnm_im, (0, 0), tnm_im)

fp = r
if not os.path.exists(fp):
  os.mkdir(fp)

fp = fp + '/' + z
if not os.path.exists(fp):
  os.mkdir(fp)

fp = fp + '/' + x
if not os.path.exists(fp):
  os.mkdir(fp)

fp = fp + '/' + y + '.jpeg'

im.save(fp, quality=50, optimize=True, progressive=True)

#i = im.tostring()

#print "Content-Type: image/png\nContent-Length: %d\n" % len(i)
#print i

loc = "http://" + s + fp
    
print "Location:     " + loc + "\r\n\r"
loc = 'COMBO: ' + loc + '\n'
sys.stderr.write(loc)
  
