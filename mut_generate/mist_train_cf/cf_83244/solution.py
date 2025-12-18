"""
QUESTION:
Design a function named `alternating_minimum_maximum_bst` that takes an array of integers and decimal numbers as input. The function should return the array arranged in a sequence where it starts with the lowest value, proceeds with the highest value, and continuously alternates between the lowest and highest values from the remaining unselected elements.
"""

def alternating_minimum_maximum_bst(array):
    array.sort()
    result = []
    while len(array) > 0:
        result.append(array.pop(0)) # Get and remove minimum value
        if len(array) > 0:
            result.append(array.pop()) # Get and remove maximum value
    return result