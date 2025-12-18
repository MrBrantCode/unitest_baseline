"""
QUESTION:
Write a function `second_largest` that takes a list of unique integers as input and returns the second highest value. The list is not sorted and contains at least two elements.
"""

def second_largest(arr):
    arr.sort()
    return arr[-2]