"""
QUESTION:
Write a function named `find_closest_collectible` that takes a player's current position as a tuple of three floats representing x, y, and z coordinates, and a list of collectibles where each collectible is a tuple containing a Vector3 object representing its coordinates and a string representing its description. The function should return the description of the closest collectible to the player's position based on the Euclidean distance.
"""

import math

def find_closest_collectible(player_position, collectibles):
    closest_distance = float('inf')
    closest_collectible = None

    for collectible in collectibles:
        collectible_position = collectible[0]
        distance = math.sqrt((player_position[0] - collectible_position.x) ** 2 +
                             (player_position[1] - collectible_position.y) ** 2 +
                             (player_position[2] - collectible_position.z) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_collectible = collectible[1]

    return closest_collectible