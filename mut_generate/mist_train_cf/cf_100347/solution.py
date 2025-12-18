"""
QUESTION:
Write a function called `haversine_cluster` that takes a reference point's latitude and longitude, and a dictionary of attractions with their corresponding coordinates. Using the Haversine formula, calculate the distances from the reference point to each attraction and group the attractions into two clusters based on their proximity to each other. The function should return the distances and the two clusters. The input dictionary keys are the attraction names and the values are tuples of latitude and longitude. The reference point and attraction coordinates are in decimal degrees format. The radius of the earth is assumed to be 6371 kilometers.
"""

import math

def haversine_cluster(lat1, lon1, attractions):
    """
    Calculate the distances from a reference point to each attraction and group the attractions into two clusters.

    Args:
    lat1 (float): The latitude of the reference point.
    lon1 (float): The longitude of the reference point.
    attractions (dict): A dictionary of attractions with their corresponding coordinates.

    Returns:
    dict: A dictionary with attraction names as keys and their distances from the reference point as values.
    list: A list of two clusters of attraction names.
    """
    # Define the Haversine formula to calculate the distance between two points
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # radius of the earth in kilometers
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d

    # Calculate the distances between the reference point and the attractions
    distances = {}
    for attraction, coords in attractions.items():
        lat2, lon2 = coords
        distance = haversine(lat1, lon1, lat2, lon2)
        distances[attraction] = distance

    # Group the attractions into two clusters based on their distances to each other
    sorted_attractions = sorted(distances, key=distances.get)
    cluster1 = sorted_attractions[:len(sorted_attractions) // 2]
    cluster2 = sorted_attractions[len(sorted_attractions) // 2:]

    return distances, [cluster1, cluster2]