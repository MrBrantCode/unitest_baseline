"""
QUESTION:
Write a function `calculate_city_distances` that calculates the distances between each city in a given Geojson collection and a reference point. The reference point is defined by the coordinates `(-106.63145, 42.86662)`. The function should use the Haversine formula to calculate the distance between two sets of coordinates. The distance should be rounded to the nearest kilometer. The function should be optimized to handle a large number of cities efficiently, processing a Geojson collection containing up to 10,000 cities within a reasonable amount of time. The function should return a dictionary where the keys are the city names and the values are the distances from the reference point.
"""

import math

def calculate_city_distances(data):
    # Reference point
    ref_lat = 42.86662
    ref_lon = -106.63145

    # Haversine formula to calculate the distance between two sets of coordinates
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # radius of the Earth in kilometers

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        distance = R * c
        return round(distance)

    # Iterate over each city in the Geojson data
    city_distances = {}
    for feature in data["features"]:
        city_lat = feature["geometry"]["coordinates"][1]
        city_lon = feature["geometry"]["coordinates"][0]
        city_name = feature["properties"]["name"]

        # Calculate the distance between the city and the reference point
        distance = haversine(ref_lat, ref_lon, city_lat, city_lon)

        city_distances[city_name] = distance

    return city_distances