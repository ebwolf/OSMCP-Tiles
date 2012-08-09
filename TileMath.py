# import just what we need from math - this keeps the syntax clean
from math import pi, log, exp, atan, tan, cos, radians

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
    xtile = (lon + 180.0) / 360.0 * n
    ytile = (1.0 - log(tan(radians(lat)) + (1 / cos(radians(lat)))) / pi) / 2.0 * n

    return (int(xtile), int(ytile))
