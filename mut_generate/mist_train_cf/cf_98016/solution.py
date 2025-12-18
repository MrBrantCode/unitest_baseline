"""
QUESTION:
Write a function called `cluster_attractions` that takes in a dictionary `attractions` where the keys are the names of the attractions and the values are tuples representing the latitude and longitude of each attraction. The function should calculate the distances between each pair of attractions using the Haversine formula and group them into two clusters based on their distances to each other. The function should return a list of two lists where each sublist contains the names of the attractions in a cluster. The order of the attractions in each cluster does not matter, but the order of the clusters does - the first cluster should be the one with the shorter average distance between its attractions.
"""

import math
import itertools

def cluster_attractions(attractions):
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

    # Calculate the distances between each pair of attractions
    distances = {}
    for (attraction1, coords1), (attraction2, coords2) in itertools.combinations(attractions.items(), 2):
        lat1, lon1 = coords1
        lat2, lon2 = coords2
        distance = haversine(lat1, lon1, lat2, lon2)
        distances[(attraction1, attraction2)] = distance

    # Group the attractions into two clusters based on their distances to each other
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    cluster1 = [sorted_distances[0][0][0], sorted_distances[0][0][1]]
    cluster2 = [attraction for attraction in attractions.keys() if attraction not in cluster1]
    return [cluster1, cluster2]