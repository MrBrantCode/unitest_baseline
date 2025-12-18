"""
QUESTION:
Compute the lateral surface area and volume of a list of frustums, each defined by their radii and slant height. The function `compute_frustum_properties` should take a list of dictionaries, where each dictionary contains the keys 'r1', 'r2', 'h', and optionally 'a1', 'a2', 'b1', 'b2' for elliptical frustums. The function should return two dictionaries containing the lateral surface areas and volumes of the frustums, respectively. The function should handle invalid inputs (negative radii or heights) by generating an error message. The function should have a time complexity not exceeding O(n log n) and provide accurate results up to 15 decimal places.
"""

from math import pi

def compute_frustum_properties(frustums):
    # Creating empty dictionaries to store the results.
    lateral_areas = {}
    volumes = {}

    for frustum in frustums:
        if not validate_input(frustum):
            print('Invalid input')
            continue

        # Computing and storing the lateral surface area and volume for each frustum.
        lateral_areas[frustum['id']] = compute_lateral_area(frustum)
        volumes[frustum['id']] = compute_volume(frustum)

    return lateral_areas, volumes


def validate_input(frustum):
    for key in ['r1', 'r2', 'h']:
        if frustum[key] < 0:
            return False
    return True


def compute_lateral_area(frustum):
    r1 = frustum['r1']
    r2 = frustum['r2']
    h = frustum['h']

    lateral_area = pi * (r1 + r2) * h
    return round(lateral_area, 15)  # Ensuring 15 decimal point precision.


def compute_volume(frustum):
    r1 = frustum['r1']
    r2 = frustum['r2']
    h = frustum['h']

    volume = (1/3) * pi * h * (r1**2 + r2**2 + r1*r2)
    return round(volume, 15)  # Ensuring 15 decimal point precision.