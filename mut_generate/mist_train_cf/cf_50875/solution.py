"""
QUESTION:
Write a function `find_uniq` that takes an array of numbers as input and returns the number that appears only once. The array contains at least 3 numbers and all numbers are equal except for one. The function should be optimized for performance to handle large arrays.
"""

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b