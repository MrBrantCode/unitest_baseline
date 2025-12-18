"""
QUESTION:
Create a function named `count_occurrences` that takes a multi-dimensional numerical array and a target number `x` as input. The function should return the total number of occurrences of `x` in the array, regardless of the depth. The array can contain integers, floating point numbers, or nested lists.
"""

def count_occurrences(arr, x):
    count = 0
    for el in arr:
        if isinstance(el, list):
            count += count_occurrences(el, x)
        elif el == x:
            count += 1
    return count