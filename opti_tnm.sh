#!/bin/bash -x
echo Optimizing TNM cache for PNG performance

cd /tiles/tnm
find -name '*.png8' -exec rename 's/png8/png/' {} \;
find -name "*.png" | nice xargs mogrify -type Palette -colors 16
find -name "*.png" | nice xargs optipng -q 

