#!/bin/bash -x
echo Making $1 into transparent PNGs

cd /osmcp/tiles/$1
find -name "*.jpeg" -exec rm {} \;
find -name "*.png" | nice xargs mogrify -auto-level -type Palette -colors 2 -transparent black -transparent-color black

