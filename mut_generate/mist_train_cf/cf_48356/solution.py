"""
QUESTION:
Write a function `sort_array` that takes an array of integers as input and sorts it in both ascending and descending order. The function should handle duplicate values and have a time complexity of O(n log n) and space complexity of O(n).
"""

def sort_array(arr):
    arr.sort()  # Sort array in ascending order
    return arr, arr[::-1]  # Return array in both ascending and descending order