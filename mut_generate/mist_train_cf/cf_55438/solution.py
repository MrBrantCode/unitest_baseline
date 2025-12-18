"""
QUESTION:
Write two functions: `array_to_set` and `symmetric_difference`. The `array_to_set` function should take an array as input and return a set. The `symmetric_difference` function should take two sets as input and return their symmetric difference, which is the set of elements that are in exactly one of the sets. The function should handle possible duplicate values within a single array by not counting a repeated element as part of the unique symmetric difference between the two arrays.
"""

def entance(arr_1, arr_2):
    return set(arr_1) ^ set(arr_2)