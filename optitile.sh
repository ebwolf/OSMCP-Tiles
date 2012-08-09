#!/bin/bash -x
echo Optimizing $1 for PNG performance

cd /osmcp/tiles/$1
find -name "*.jpeg" -exec rm {} \;
find -name "*.jpg" -exec rm {} \;
find -name "*.png" | nice xargs mogrify -type Palette
find -name "*.png" | nice xargs optipng -q

