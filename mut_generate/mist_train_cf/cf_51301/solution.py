"""
QUESTION:
Write a function named `array_difference` that takes two integer arrays `arr_a` and `arr_b` as input. The function should return a new array containing the differences between corresponding elements in `arr_a` and `arr_b`. If `arr_a` and `arr_b` are of different lengths, the function should return an error message.
"""

def array_difference(arr_a, arr_b):
    if len(arr_a) != len(arr_b):
        return "Arrays are of unequal lengths."
    else:
        return [a - b for a, b in zip(arr_a, arr_b)]