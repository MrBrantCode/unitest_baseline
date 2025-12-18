"""
QUESTION:
Write a function `calculate_gravel` that takes an integer `path_weight` as input and returns a list of three integers representing the minimum quantities of 3-ton, 2-ton, and 1-ton gravels needed to reach the given `path_weight`. The function should use a greedy approach to minimize the total quantity of gravel pieces. The input `path_weight` is guaranteed to be a non-negative integer.
"""

def calculate_gravel(path_weight):
    # Assume that the order of the gravel types is from
    # heaviest to lightest to have the minimum amount of pieces.

    weights = [3, 2, 1] 
    quantities = [0, 0, 0] 

    for i, weight in enumerate(weights):
        while path_weight - weight >= 0:
            quantities[i] += 1
            path_weight -= weight            

    return quantities