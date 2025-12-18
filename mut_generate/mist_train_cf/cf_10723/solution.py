"""
QUESTION:
Create a function `search_list` that takes a list of integers `l` and a target integer `v` as input, and returns the index of the first occurrence of `v` in `l`. If `v` is not found, return -1. The function should be case-insensitive, handle large lists efficiently, and correctly handle empty lists and negative values of `v`.
"""

def search_list(l, v):
    if not l:
        return -1
    
    for i, item in enumerate(l):
        if item == v:
            return i
    
    return -1