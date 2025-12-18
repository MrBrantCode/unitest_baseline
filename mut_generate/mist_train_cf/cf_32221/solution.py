"""
QUESTION:
Implement a function named `calculate_shortest_route` that takes two parameters: a list of `locations` and a 2D list of `distances` where the element at index (i, j) represents the distance from location i to location j. The function should return the optimized route as a list of locations in the order they should be visited to minimize the total distance traveled, assuming the route starts and ends at the first location.
"""

import itertools

def calculate_shortest_route(locations, distances):
    min_distance = float('inf')
    optimized_route = []

    for route in itertools.permutations(range(len(locations))):
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[route[i]][route[i+1]]
        distance += distances[route[-1]][route[0]]

        if distance < min_distance:
            min_distance = distance
            optimized_route = route

    return [locations[i] for i in optimized_route]