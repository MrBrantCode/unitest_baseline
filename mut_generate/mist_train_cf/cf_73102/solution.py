"""
QUESTION:
Create a function called `successive_pairs` that takes a list as input and returns a list of tuples. Each tuple should contain two successive elements from the input list. The function should return all possible successive pairs from the input list.
"""

def successive_pairs(lst):
    return list(zip(lst, lst[1:]))