"""
QUESTION:
Write a function `find_max` that takes an array of at least 5 integers as input, finds the maximum value, and returns it along with the total number of comparisons made during the search. The function should handle the case when the input array is empty, in which case it should return `None` for the maximum value and `0` for the number of comparisons.
"""

def find_max(arr):
    if len(arr) == 0:
        return None, 0

    max_value = arr[0]
    comparisons = 0

    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value, comparisons