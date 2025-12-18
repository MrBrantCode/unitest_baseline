"""
QUESTION:
Implement the `optimize` function, which takes a list of colors represented by integers as input and returns a list of 4 indices representing the optimized combination of colors that minimizes the cost. The cost is calculated based on the absolute difference between the selected colors: `abs(data[i] - data[j]) + abs(data[j] - data[k]) + abs(data[k] - data[l])` for colors at indices (i, j, k, l).
"""

import itertools

def optimize(data):
    min_cost = float('inf')
    optimized_combination = None
    for i, j, k, l in itertools.combinations(range(len(data)), 4):
        cost = abs(data[i] - data[j]) + abs(data[j] - data[k]) + abs(data[k] - data[l])
        if cost < min_cost:
            min_cost = cost
            optimized_combination = [i, j, k, l]
    return optimized_combination