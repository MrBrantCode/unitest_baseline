"""
QUESTION:
Write a function `calculateDistance` that takes two JSON objects representing geographical points as input and returns the distance between them in kilometers. Each JSON object has the structure `{"geometry": {"type": "Point", "coordinates": [longitude, latitude]}}`. The function should use the Haversine formula to calculate the distance. Assume the radius of the Earth is 6371 kilometers.
"""

import math

def calculateDistance(point1, point2):
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = point1["geometry"]["coordinates"][1], point1["geometry"]["coordinates"][0]
    lat2, lon2 = point2["geometry"]["coordinates"][1], point2["geometry"]["coordinates"][0]

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance