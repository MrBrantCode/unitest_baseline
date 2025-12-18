"""
QUESTION:
Implement a function `calculate_distances(geolocations: List[Dict[str, float]]) -> List[float]` that takes a list of dictionaries representing geolocations, where each dictionary contains "latitude" and "longitude" keys with numerical values, and returns a list of distances in kilometers between each pair of geolocations. The distance should be calculated using the Haversine formula, taking into account the curvature of the Earth, and rounded to the nearest whole number.
"""

from typing import List, Dict
import math

def calculate_distances(geolocations: List[Dict[str, float]]) -> List[float]:
    R = 6371  # Earth's radius in kilometers
    distances = []
    for i in range(len(geolocations)):
        lat1, long1 = math.radians(geolocations[i]['latitude']), math.radians(geolocations[i]['longitude'])
        for j in range(len(geolocations)):
            if i == j:
                distances.append(0.0)
            else:
                lat2, long2 = math.radians(geolocations[j]['latitude']), math.radians(geolocations[j]['longitude'])
                delta_lat = lat2 - lat1
                delta_long = long2 - long1
                a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long/2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                distance = R * c
                distances.append(round(distance))
    return distances