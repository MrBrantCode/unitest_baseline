"""
QUESTION:
Implement a function `convertToRectangular` that takes the latitude and longitude in degrees as input and returns the corresponding rectangular coordinates (x, y, z) using the formulas: x = cos(latitude) * cos(longitude), y = cos(latitude) * sin(longitude), and z = sin(latitude). The input latitude and longitude should be converted to radians before applying the formulas.
"""

import math

def convertToRectangular(latitude, longitude):
    x = math.cos(math.radians(latitude)) * math.cos(math.radians(longitude))
    y = math.cos(math.radians(latitude)) * math.sin(math.radians(longitude))
    z = math.sin(math.radians(latitude))
    return (x, y, z)