"""
QUESTION:
Write a function `sum_prefix(arr)` that takes a list of integers as input and returns the cumulative sum of unique integers, each prefixed by the absolute value of the smallest integer in the collection. The input list should only consist of negative integers, and the function should return None if the list is empty, does not exist, or contains non-negative integers.
"""

def sum_prefix(arr):
    if not arr or type(arr) != list:
        return None
    unique_arr = set(arr)
    if not all(i < 0 for i in unique_arr):
        return None
    min_int = min(unique_arr)
    return sum(unique_arr) + min_int * len(unique_arr)