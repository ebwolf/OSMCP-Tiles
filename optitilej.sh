#!/bin/bash -x
echo Optimizing $1 for JPEG performance

cd /osmcp/tiles/$1
find -name "*.png" -exec rm {} \;
find -name "*.jpeg" | nice xargs jpegoptim --strip-all -m30

