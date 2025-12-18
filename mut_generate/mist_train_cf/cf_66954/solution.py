"""
QUESTION:
Implement a function `max_pair(arr)` that takes a pre-sorted list of unique integers in ascending order as input and returns a tuple containing the pair of elements with the highest absolute value sum. The result should be in the form of a tuple, with the smaller number first. Assume the input list has at least two elements. The function should have a time complexity of O(1).
"""

def max_pair(arr):
    max_pair = (arr[-2], arr[-1]) 
    return max_pair