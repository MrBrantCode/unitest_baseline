"""
QUESTION:
Given a list of integers representing package weights and an integer representing the truck's weight capacity, write a function `max_weight` that takes these two parameters and returns the maximum total weight that can be loaded onto the truck without exceeding its capacity.
"""

import itertools

def entrance(weights, capacity):
    max_weight = 0
    for r in range(1, len(weights) + 1):
        combinations = itertools.combinations(weights, r)
        for combo in combinations:
            if sum(combo) <= capacity and sum(combo) > max_weight:
                max_weight = sum(combo)
    return max_weight