"""
QUESTION:
Write a function `find_first_repeating` that takes an array of integers as input and returns the first repeating element that appears more than once. The function should have a time complexity of O(n). If no such element is found, return -1. The function should find the first repeating element based on the order of elements in the array.
"""

def find_first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return -1