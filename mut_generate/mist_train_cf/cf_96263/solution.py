"""
QUESTION:
Write a function `get_reversed_n_items` that takes a list and an integer `n` as input, and returns the first `n` items from the list in reverse order without modifying the original list.
"""

def get_reversed_n_items(lst, n):
    return lst[:n][::-1]