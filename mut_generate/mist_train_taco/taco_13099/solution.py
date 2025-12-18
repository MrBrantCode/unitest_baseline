"""
QUESTION:
Convert DD (decimal degrees) position to DMS (degrees, minutes, seconds).

##### Inputs:
`dd_lat` and `dd_lon` 2 strings representing the latitude and the longitude in degree -i.e. 2 floats included in [-90, 90] and [-180, 180]. Note that latitude 0 is north, longitude 0 is east.

##### Outputs:
A tuple of DMS latitudes formated as follows:
`DDD*mm'ss.sss"C`

With:
- `DDD`: degrees
- `mm`: minutes
- `ss.sss`: seconds rounded to 3 decimals
- `C`: first letter uppercase of the cardinal direction

##### ressources
about WGS 84 on [Wikipedia](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84)
"""

from math import floor

def convert_dd_to_dms(dd_lat: str, dd_lon: str) -> tuple:
    def convert(dd: float, direction: str) -> str:
        degrees = floor(dd)
        seconds = round(dd % 1 * 3600000)
        return '%03d*%02d\'%06.3f"%s' % (degrees, seconds // 60000, seconds % 60000 / 1000, direction)
    
    dd_lat = float(dd_lat)
    dd_lon = float(dd_lon)
    
    dms_lat = convert(abs(dd_lat), 'N' if dd_lat >= 0 else 'S')
    dms_lon = convert(abs(dd_lon), 'E' if dd_lon >= 0 else 'W')
    
    return (dms_lat, dms_lon)