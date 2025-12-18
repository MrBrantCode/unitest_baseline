"""
QUESTION:
Write a function `find_elements` that takes a multi-dimensional array as input and returns the second, third, and fourth smallest unique numbers in ascending order. The input array can have uneven internal array dimensions and may contain repeated numbers. If the array has less than 4 unique numbers, return "The array does not have enough unique numbers". The solution should be as efficient as possible.
"""

import heapq

def find_elements(arr):
    flattened = set([num for sublist in arr for num in sublist])
    smallest_nums = heapq.nsmallest(4, flattened)
    return smallest_nums[1:] if len(smallest_nums) > 3 else "The array does not have enough unique numbers"