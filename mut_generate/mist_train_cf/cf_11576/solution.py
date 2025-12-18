"""
QUESTION:
Implement a function `convert_coordinates_to_longitude_latitude` that takes X and Y coordinates as input and returns the corresponding longitude and latitude. The conversion should account for the curvature of the Earth and the geoid shape, and be accurate to at least 6 decimal places. The function should not rely on external libraries or APIs, and should have a time complexity of O(1) or O(log n) and a space complexity of O(1).
"""

import math

def convert_coordinates_to_longitude_latitude(X, Y):
    R = 6371  # radius of the Earth in kilometers

    longitude = X / (R * math.cos(Y))
    latitude = math.atan(math.exp(Y / R)) - (math.pi / 4)

    return round(longitude, 6), round(latitude, 6)