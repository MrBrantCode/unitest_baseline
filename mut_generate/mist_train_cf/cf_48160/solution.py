"""
QUESTION:
Create a function `remove_duplicate(seq)` that takes a list of integers as input and returns a new list with all duplicate elements removed, preserving the original order.
"""

def remove_duplicate(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]