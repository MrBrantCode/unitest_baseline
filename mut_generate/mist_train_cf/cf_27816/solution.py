"""
QUESTION:
Calculate the total distance traveled by an object based on its geographical coordinates. Implement the `calculate_total_distance` function that takes a list of geographical coordinates as input, where each coordinate is a tuple of latitude and longitude values. The function should return the total distance traveled in kilometers. Use the Haversine formula to calculate the distance between two coordinates, assuming the Earth's radius is approximately 6371 kilometers. The input list will contain at least two coordinates.
"""

from typing import List, Tuple
import math

def calculate_total_distance(geographical_coordinates: List[Tuple[float, float]]) -> float:
    total_distance = 0.0
    for i in range(len(geographical_coordinates) - 1):
        lat1, lon1 = geographical_coordinates[i]
        lat2, lon2 = geographical_coordinates[i + 1]
        radius = 6371  # Radius of the Earth in kilometers

        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)

        a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = radius * c
        total_distance += distance

    return total_distance