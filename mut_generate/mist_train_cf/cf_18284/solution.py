"""
QUESTION:
Calculate the distance between each city in a Geojson collection and a reference point. The function `calculate_distances` should take a Geojson object and a reference point (latitude and longitude) as input, and return a dictionary with city names as keys and distances as values. The distance should be calculated using the Haversine formula and rounded to the nearest kilometer. The function should be able to handle a Geojson collection containing up to 10,000 cities within a reasonable amount of time.
"""

import math

def calculate_distances(geojson, ref_lat, ref_lon):
    distances = {}

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
    for feature in geojson["features"]:
        city_lat = feature["geometry"]["coordinates"][1]
        city_lon = feature["geometry"]["coordinates"][0]
        city_name = feature["properties"]["name"]

        # Calculate the distance between the city and the reference point
        distances[city_name] = haversine(ref_lat, ref_lon, city_lat, city_lon)

    return distances