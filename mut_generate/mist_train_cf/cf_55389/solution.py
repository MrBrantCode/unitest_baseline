"""
QUESTION:
Write a function `calculate_sum` that calculates the summation of the reciprocal of each integral element within a deeply nested multidimensional structure. The function should work with lists or tuples of arbitrary depth and should only include integral elements in the summation.
"""

def entance(nested_list):
    total = 0
    for i in nested_list:
        if isinstance(i, (list, tuple)):
            total += entance(i)
        elif isinstance(i, int):
            total += 1/i
    return total