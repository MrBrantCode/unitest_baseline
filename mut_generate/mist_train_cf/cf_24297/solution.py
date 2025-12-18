"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes a list of integers as input and returns a new list containing all unique elements from the original list, in the original order. The function should preserve the order of elements and not contain any duplicate values.
"""

def remove_duplicates(arr):
    new_arr = []
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
            new_arr.append(i)
    return new_arr