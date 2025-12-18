"""
QUESTION:
Implement a function `merge_sort(L1, L2)` that takes two lists `L1` and `L2` as input, merges them into a single list, and returns the sorted merged list in ascending order. The function should be able to handle large input lists efficiently.
"""

def merge_sort(L1, L2):
    L3 = L1 + L2  
    L3.sort()  
    return L3 