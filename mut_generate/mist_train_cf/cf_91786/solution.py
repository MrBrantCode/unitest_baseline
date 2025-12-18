"""
QUESTION:
Write a function `calculate_city_distances` that takes a Geojson object representing a FeatureCollection of cities with point geometries, and a reference point's coordinates as a tuple of (longitude, latitude). The function should calculate the distance between each city and the reference point using the Haversine formula, round the distance to the nearest kilometer, and return a dictionary where the keys are the city names and the values are the corresponding distances. The radius of the Earth is assumed to be 6371 kilometers.
"""

from math import radians, sin, cos, sqrt, atan2

def calculate_city_distances(geojson, ref_point):
    """
    Calculate the distance between each city in the Geojson object and a reference point.

    Args:
    geojson (dict): A Geojson object representing a FeatureCollection of cities with point geometries.
    ref_point (tuple): The reference point's coordinates as a tuple of (longitude, latitude).

    Returns:
    dict: A dictionary where the keys are the city names and the values are the corresponding distances.
    """
    R = 6371  # radius of the Earth in kilometers
    city_distances = {}

    for feature in geojson['features']:
        city_name = feature['properties']['name']
        city_coordinates = feature['geometry']['coordinates']

        # convert coordinates to radians
        lat1, lon1, lat2, lon2 = map(radians, [ref_point[1], ref_point[0], city_coordinates[1], city_coordinates[0]])

        # calculate the differences in coordinates
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # calculate the distance using the Haversine formula
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        city_distances[city_name] = round(distance)

    return city_distances