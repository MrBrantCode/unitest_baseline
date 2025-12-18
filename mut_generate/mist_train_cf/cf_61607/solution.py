"""
QUESTION:
Find the missing numbers in an arithmetic progression given an array of integers where some values were removed, excluding the first and last values. The function should return the removed values in the order they appear in the original array.

The array `arr` has a length between 5 and 2000, and each element `arr[i]` is between 0 and 10^6. The function `find_missing_numbers(arr)` should return a list of integers representing the removed values in the original order.
"""

def find_missing_numbers(arr):
    difference = (arr[-1] - arr[0]) // (len(arr) - 1)
    original = set(range(arr[0], arr[-1]+1, difference))
    removed = original.difference(arr)
    return sorted(list(removed))