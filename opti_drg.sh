#!/bin/bash -x
echo Optimizing DRG cache for PNG performance

cd /osmcp/tiles/drg
find -name "*.jpeg" -exec rm {} \;
find -name "*.jpg" -exec rm {} \;
find -name "*.png" | nice xargs mogrify -type Palette -colors 16
find -name "*.png" | nice xargs optipng -q

