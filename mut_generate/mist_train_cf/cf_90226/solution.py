"""
QUESTION:
Write a function `search_index(lst, target)` that takes a list `lst` of numbers and a target number `target` as input, and returns the index of `target` in `lst` if found. If `target` is not found in `lst`, return -1. Do not use the built-in `index` function or any other built-in functions for searching. Handle edge cases such as empty lists, lists with duplicate elements, and lists with negative numbers, and ensure a time complexity of O(n).
"""

def search_index(lst, target):
    if not lst:
        return -1  # Handle empty list case
    
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1  # Element not found case