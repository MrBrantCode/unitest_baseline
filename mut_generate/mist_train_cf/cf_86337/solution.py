"""
QUESTION:
Write a function `find_first_repeating(arr)` that finds the first repeating element in an array of integers, with a time complexity of O(n) and without using any additional data structures other than variables for storing intermediate results. If no such element is found, return -1.
"""

def find_first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1