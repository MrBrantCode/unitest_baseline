"""
QUESTION:
Given an array of integers, write a function `smallest_positive` that finds the smallest positive integer missing from the array. The function should return the smallest positive integer that is not present in the array. Assume the input array may contain negative numbers and zeros. The function should return an integer value.
"""

def smallest_positive(arr):
    s = set(arr)
    i = 1
    while i in s:
        i += 1
    return i