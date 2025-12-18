"""
QUESTION:
Create a function called `convert_to_decimal` that takes in the degrees, minutes, and seconds of a coordinate, its direction ('N', 'S', 'E', 'W'), and the observer's latitude (in degrees) to convert the coordinate to decimal format, considering the Earth's curvature and the observer's position relative to the Equator and Prime Meridian.
"""

import math

EARTH_RADIUS = 6371  # km
EQUATORIAL_CIRCUMFERENCE = 40075.017  # km
DEG_TO_RAD = math.pi / 180.0
RAD_TO_DEG = 180.0 / math.pi

def convert_to_decimal(degrees, minutes, seconds, direction, observer_latitude):
    """
    Converts coordinates in degrees, minutes, and seconds to decimal format
    using the observer's position relative to the Equator and Prime Meridian.
    """
    decimal_degrees = degrees + minutes/60.0 + seconds/3600.0

    sign = 1 if direction in ['N', 'E'] else -1

    if direction in ['N', 'S']:
        circumference = EQUATORIAL_CIRCUMFERENCE * math.cos(observer_latitude * DEG_TO_RAD)
        decimal_coord = sign * decimal_degrees * circumference / 360.0
    else:
        circumference = EQUATORIAL_CIRCUMFERENCE
        decimal_coord = sign * decimal_degrees * circumference / 360.0 * math.cos(observer_latitude * DEG_TO_RAD)

    decimal_coord *= math.pi * EARTH_RADIUS / 180.0

    return decimal_coord