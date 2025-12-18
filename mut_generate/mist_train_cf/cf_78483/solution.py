"""
QUESTION:
Write a function named `max_difference` that takes an array of integers as input. For each distinct integer in the array, calculate its maximum difference with any other integer in the array. Return a 2D array where each sub-array is of the form [number, maximum difference] and is sorted in descending order based on the maximum difference.
"""

def max_difference(array):
    res = []
    for value in set(array):
        max_diff = max(abs(value - x) for x in array)
        res.append([value, max_diff])
        
    return sorted(res, key = lambda x : x[1], reverse = True)