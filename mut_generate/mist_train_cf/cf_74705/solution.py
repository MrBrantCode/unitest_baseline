"""
QUESTION:
Write a function `find_smallest` that takes an array of mixed data types as input and returns the smallest integer in the array. The function should handle non-integer values and exclude Booleans. If no integers are found, the function should return a meaningful result.
"""

def find_smallest(arr):
    smallest = float('inf')
    for i in arr:
        if type(i) is int and i < smallest:
            smallest = i
    return smallest if smallest != float('inf') else "No integers found"