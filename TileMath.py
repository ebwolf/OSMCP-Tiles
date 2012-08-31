# import just what we need from math - this keeps the syntax clean
from math import pi, log, exp, atan, tan, cos, radians, floor

# Safely computes the secant of r
def sec(r):
    c = cos(r)
    
    if c == 0:
        c = 0.001
        
    return(1 / c)
        

# Takes lat/lon and returns a Google EPSG:900913 coordinate pair
def WGS84toGoogle(lon, lat):
    x = lon * 20037508.34 / 180
    y = log(tan((90 + lat) * pi / 360)) / (pi / 180)
    y = y * 20037508.34 / 180

    return (round(x,2), round(y,2))

# Takes a Google EPSG:900913 coordinate pair and returns lat/lon
def GoogletoWGS84(x, y):
    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / pi * (2 * atan(exp(lat * pi / 180)) - pi / 2)
    
    return (lon, lat)

# Takes lat/lon in WGS84 + zoom level and returns the X, Y for the tile
def WGS84toTileXY(lat, lon, zoom):
    n = 2.0 ** zoom
    xtile = ((lon + 180.0) / 360.0) * n
    
    rlat = radians(lat)
#    t = tan(rlat)
#    s = secant(rlat)
#    print t, s
#    l = log(t + s)
#    l = l / pi
#    l = 1.0 - l
#    ytile = (1.0 - (log( tan(radians(lat)) + secant(radians(lat)) )  / pi)) / 2.0 * n
#    ytile = l / 2 * n 
    ytile = (1.0 - log(tan(rlat) + (1 / cos(rlat))) / pi) / 2.0 * n
    return (int(floor(xtile)), int(floor(ytile)))

# Converts pixel coordinates in given zoom level of pyramid to EPSG:900913
def PixelsToMeters(px, py, zoom):

    # tileSize = 256
    # radiusEarth = 6378137 meters
    #
    # R0 = 2 * math.pi * radiusEarth / tileSize
    # R0 = 156543.03392804062
    r0 = 156543.03392804062

    # originShift = 2 * math.pi * radiusEarth / 2.0
    os = 20037508.342789244

    # res = R0 / (2**zoom)
    res = r0 / (2**zoom)
            
    mx = px * res - os
    my = py * res - os
    return mx, my
                                         

# Returns bounds of the given tile in EPSG:900913 coordinates
def TileXYZtoGoogle(tx, ty, zoom):
    tileSize = 256
    radiusEarth = 6378137 # meters
    
    # initial resolution
    r0 = 2 * pi * radiusEarth / tileSize
    # R0 = 156543.03392804062
    #r0 = 156543.0339

    # origin shift
    os = 2 * pi * radiusEarth / 2.0
    #os = 20037508.34

    # res = R0 / (2**zoom)
    res = r0 / (2**zoom)

    #ty = 2** zoom - 1 - ty # Expects TMS y coordinate
    ty = (2** zoom - 1) - ty # Expects TMS y coordinate
    
    minx = tx * 256 * res - os
    miny = ty * 256 * res - os
    maxx = (tx + 1) * 256 * res - os
    maxy = (ty + 1) * 256 * res - os
    
    return ( minx, miny, maxx, maxy )
    
# Unit tests
if __name__ == '__main__':
    import sys, os
    (x,y) = WGS84toTileXY(0, 0, 1)
    print "WGS84toTileXY(0,0,1) -> (" + str(x) + "," + str(y) + ")"
    (x,y) = WGS84toTileXY(89, 179, 1)
    print "WGS84toTileXY(89,179,1) -> (" + str(x) + "," + str(y) + ")"
    (x,y) = WGS84toTileXY(-89, -179, 1)
    print "WGS84toTileXY(-89,-179,1) -> (" + str(x) + "," + str(y) + ")"
    