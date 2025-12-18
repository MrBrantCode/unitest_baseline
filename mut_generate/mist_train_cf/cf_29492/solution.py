"""
QUESTION:
Implement a function `calculate_total_distance(friend_towns, home_to_town_distances)` that calculates the total distance traveled by friends. The function should take in a list of tuples `friend_towns` where each tuple contains a friend's name and the town they are visiting, and a dictionary `home_to_town_distances` mapping town names to their distances from the friend's home. The function should iterate through `friend_towns`, check if each town is present in `home_to_town_distances`, and calculate the total distance traveled by the friends based on the distances to the towns they visited. The function should handle cases where a friend's town is not present in `home_to_town_distances`.
"""

import math

def calculate_total_distance(friend_towns, home_to_town_distances):
    total_distance = 0
    last_distance = 0
    for friend, town in friend_towns:
        if town in home_to_town_distances:
            distance = home_to_town_distances[town]
            if total_distance == 0:
                total_distance += distance
                last_distance = distance
            else:
                total_distance += math.sqrt(distance ** 2 - last_distance ** 2)
                last_distance = distance
    return total_distance