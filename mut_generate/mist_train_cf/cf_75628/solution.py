"""
QUESTION:
Write a function `find_max_combo(arr)` that takes an array of integers as input and returns the two array elements contributing to the maximal combined numerical value. If there are multiple pairs with the maximum sum, return any pair. The function should have a time complexity of O(n log n) or better.
"""

def find_max_combo(arr):
    arr.sort()
    return [arr[-2], arr[-1]]