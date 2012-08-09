
# State of Colorado

# Colorado
bbox = ( -109.05, 37.0, -102.05, 41.0 )

caches = [
    ( "drg", 1, 20 ),
    ( "naip", 1, 20 ),
    ( "tnm", 16, 20 ),
    ( "idx", 1, 20 ),
    ( "bnd", 1, 20 )
    ]
    
tnm_url = 'http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile'

tc_root = '/osmcp/tiles/'

def cacheZoom(c):
    for cache in caches:
        if cache[0] == c:
            return(cache[1], cache[2])