"""
QUESTION:
Design a function `median_distance` that takes an integer list as input, calculates the median, and returns a list sorted by the distance of each element from the median. If there's a tie, elements should be sorted based on their natural order. The input list will contain at least 3 distinct integer elements and will not exceed 10000 elements.
"""

import statistics

def median_distance(nums):
    median = statistics.median(nums)
    return sorted(nums, key=lambda x: (abs(x - median), x))