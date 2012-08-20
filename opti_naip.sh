#!/bin/bash -x
echo Optimizing NAIP for JPEG performance

cd /tiles/naip
find -name "*.png" -exec rm {} \;
find -name "*.jpeg" | nice xargs jpegoptim --strip-all -m30

