"""
QUESTION:
Write a function `find_first_repeating` that takes an array of integers as input and returns the first repeating element that appears more than once. If no such element is found, return -1. The time complexity of the solution should be O(n).
"""

def find_first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return -1