#!/usr/bin/python

#
# ccheck.cgi
#
# Checks to see if the requested layer is cached
#

import sys, os, imghdr, uuid

# Switch server names as needed
s = os.environ['SERVER_NAME']

r = '/tiles/'

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

# Root is last
l -= 1
r = '/tiles/' + parts[l]

# TNM Vector Basemap Large Scale Local TileCache
tcp = r + '/' + z + '/' + x + '/' + y + '.png'
tcj = r + '/' + z + '/' + x + '/' + y + '.jpeg'

import Image, ImageDraw, ImageFont

im = Image.new("RGB", (256,256), "#000000")
draw = ImageDraw.Draw(im)
font = ImageFont.load("arial10.pil")

fn = '/tiles/check/' + str(uuid.uuid4()) + '.png'


if os.path.exists(tcp) or os.path.exists(tcj):
	for i in range(0,2):
		cx = int(x) * 2 + i
		for j in range(0,2):
			cy = int(y) * 2 + i
  
			cp = r + '/' + str(int(z)+1) + '/' + str(cx) + '/' + str(cy)
			cpp = cp + '.png'
			cpj = cp + '.jpeg'
  
			box = [(128 * i) + 1, (128 * j) + 1, (128 * i) + 126, (128 * j) + 126]
  
			if os.path.exists(cpp) or os.path.exists(cpj):
				draw.rectangle(box, fill=(0,255,0))
			else:
				draw.rectangle(box, fill=(255,0,0))
        
			#chk = cpj + "\n"
			#sys.stderr.write(chk)


			if os.path.exists(cpp) or os.path.exists(cpj):
				draw.rectangle(box, fill=(0,255,0))
			else:
				draw.rectangle(box, fill=(255,0,0))
				
			zs = "Z:" + str(int(z) + 1)
			tx = box[0] + (box[2] - box[0]) / 2 - 10
			ty = box[1] + (box[3] - box[1]) / 2 - 4
			draw.text((tx, ty), zs, font=font)
else:
	box = [2, 2, 254, 254]
	draw.rectangle(box, fill=(255,0,0))
	zs = "Z:" + z
	tx = box[0] + (box[2] - box[0]) / 2 - 10
	ty = box[1] + (box[3] - box[1]) / 2 - 4
	draw.text((tx,ty), zs, font=font)
	
  
im.save(fn, "PNG")

#print "Location:     " + loc + '\r\n\r'

print "Location:     http://" + s + fn + '\r\n\r'

sys.exit(0)
