"""
QUESTION:
Write a function `augment_by_indices(arr, idx)` that takes a list of unique integers `arr` and a list of indices `idx` as input. The function should return a new list where each element in `arr` at index `i` is multiplied by 2 if `i+1` is in `idx`, and remains unchanged otherwise. The indices in `idx` are 1-based and are guaranteed to be within the bounds of `arr`.
"""

def augment_by_indices(arr, idx):
    return [x*2 if (i+1) in idx else x for i, x in enumerate(arr)]