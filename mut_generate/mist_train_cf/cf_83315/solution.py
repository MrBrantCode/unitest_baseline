"""
QUESTION:
Write a function `find_max_in_2D` that takes a 2D list of integers as input, where each sub-list can be of varying length. The function should return the maximum number among all sub-lists. If a sub-list is empty, it should be treated as if its maximum is 0. The time complexity of the function should be better than O(n^2).
"""

def find_max_in_2D(lst):
    return max((max(sub, default=0) for sub in lst), default=0)