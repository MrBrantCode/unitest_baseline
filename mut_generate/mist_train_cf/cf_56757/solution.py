"""
QUESTION:
Given an array of distinct integers, write a function `find_pair` that finds the pair of elements with the highest arithmetic sum. The function should return the pair of elements and their sum. The input array is not empty and contains at least two elements. The function should be efficient and handle arrays of any size.
"""

def find_pair(arr):
    # Initialize max_sum and pair variables
    max_sum = float('-inf')
    pair = None

    # Sort the array
    arr.sort()

    # The pair of elements with highest sum would be the last two elements
    pair = (arr[-1], arr[-2])
    max_sum = pair[0] + pair[1]

    return pair, max_sum