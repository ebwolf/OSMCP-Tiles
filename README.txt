OSMCP-Tiles

A handful of scripts for managing the OSMCP TileCache.

The OpenStreetMap platform relies on a Google-style tile cache. 
The "View" bit is based on OpenLayers and _could_ directly hit 
the WMS services provided by The National Map. But the "Edit" bit
is based on Potlatch2 and can only use a Google-style cache.

You could use something like Whoots to trick Potlatch2 into thinking 
a WMS is a tile cache but it's really slow. For that matter, you could
use tcr.cgi below to do the same thing :P

Instead of a simple redirect, we are using TileCache to build local caches.
TileCache seems to best run as FastCGI on our servers. There may be other
ways to speed up the cache.

Most of these scripts are geared towards managing the caches.

Right now, there are four caches:

TNM - The National Map Vector Basemap

  http://navigator.er.usgs.gov/tiles/tcr.cgi/$z/$x/$y.png

  Uses tcr.cgi to switch between the TNM Small Scale cache and the 
  locally managed cache:

    http://raster1.nationalmap.gov/ArcGIS/rest/services/TNM_Small_Scale_Imagery/MapServer
    http://raster.nationalmap.gov/ArcGIS/rest/services/TNM_Large_Scale_Imagery/MapServer

NAIP - High Resoloution Aerial Imagery

  http://navigator.er.usgs.gov/tiles/tilecache.cgi/1.0.0/naip/$z/$x/$y
  
  JPEG cache based on:
  
    http://raster.nationalmap.gov/ArcGIS/rest/services/TNM_Large_Scale_Imagery_Overlay/MapServer
    
DRG - Scanned Topographic Quads

  http://navigator.er.usgs.gov/tiles/tilecache.cgi/1.0.0/drg/$z/$x/$y
  
  PNG8 cache based on:
  
    http://raster.nationalmap.gov/ArcGIS/rest/services/DRG/TNM_Digital_Raster_Graphics/MapServer
    
IDX - Quad Index
 
  http://navigator.er.usgs.gov/tiles/tilecache.cgi/1.0.0/idx/$z/$x/$y
  
  PNG8 cache based on:
  
    http://services.nationalmap.gov/ArcGIS/rest/services/map_indices/MapServer
  
  
  