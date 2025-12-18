"""
QUESTION:
Write a function `find_first_repeating(arr)` that takes an array of integers as input and returns the first repeating element that appears more than once. If no such element is found, return -1. The function should have a time complexity of O(n) and should not use any additional data structures other than variables for storing intermediate results, but the restriction of not using additional data structures is relaxed to use a set for efficient lookup.
"""

def find_first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1