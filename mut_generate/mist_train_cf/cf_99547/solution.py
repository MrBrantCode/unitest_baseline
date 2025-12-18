"""
QUESTION:
Write a function `second_smallest` that takes a list of numbers as input and returns the second smallest number. The list may contain duplicate values and can be unsorted. Use the heapq module to solve this problem. The function should return the second smallest number.
"""

import heapq
def second_smallest(numbers):
    return heapq.nsmallest(2, numbers)[1]