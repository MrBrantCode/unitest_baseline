"""
QUESTION:
Write a function called `flatten_and_sum` that takes a nested list of integers as input, recursively flattens the list, and returns the sum of all the elements in the list. The input list can contain integers and nested lists of any depth.
"""

def flatten_and_sum(lst):
    if isinstance(lst, int):
        return lst
    else:
        sum = 0
        for elem in lst:
            sum += flatten_and_sum(elem)
        return sum