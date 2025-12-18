"""
QUESTION:
Find the endmost triplet of word clusters in a given string. 

Write a function named `find_endmost_triplet` that takes a string of alphanumeric characters as input. The string contains word clusters, which are sequences of alphanumeric characters separated by a space. The function should return the last sequence of three word clusters in the string. If the string contains less than three word clusters, return None.
"""

import re

def find_endmost_triplet(s):
    # Split the string into word clusters
    clusters = s.split()

    # Initialize an empty list to store found triplets
    triplets = []

    # Use a loop to find all triplets
    for i in range(len(clusters) - 2):
        # Concatenate the current cluster with the next two clusters
        triplet = " ".join(clusters[i:i+3])
        # Add this triplet to the list of found triplets
        triplets.append(triplet)

    # The last triplet in the list is the endmost triplet of word clusters in the text
    return triplets[-1] if triplets else None