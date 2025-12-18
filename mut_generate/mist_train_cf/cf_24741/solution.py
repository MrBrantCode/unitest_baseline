"""
QUESTION:
Write a function `get_unique_pairs` that takes a list of integers as input and returns all unique pairs of numbers from the list. The order of the pairs does not matter and the pair (a, b) is considered the same as (b, a).
"""

def get_unique_pairs(lst):
    """Returns all unique pairs of numbers from the input list."""
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            pairs.append((lst[i], lst[j])) 
    return pairs