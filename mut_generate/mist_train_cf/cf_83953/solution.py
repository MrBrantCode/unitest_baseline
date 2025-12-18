"""
QUESTION:
Write a Python function `get_exclusive_integers(array)` that takes an array of tuples, where each tuple contains a range of integers, and returns a sorted list of all integers in these ranges, excluding the start and end of each range, with no duplicates.
"""

def get_exclusive_integers(array):
    res = set()
    for tup in array:
        res.update(range(tup[0]+1,tup[1]))
    return sorted(list(res))