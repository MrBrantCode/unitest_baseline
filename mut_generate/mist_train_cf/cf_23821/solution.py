"""
QUESTION:
Write a function `findSmallestMissing` that takes a list of integers as input and returns the smallest positive integer that is not in the list. The function should start checking from 1 and return the first missing positive integer.
"""

def findSmallestMissing(arr):
    smallest_missing = 1
    
    for num in arr:
        if num == smallest_missing:
            smallest_missing += 1
    
    return smallest_missing