"""
QUESTION:
Write a function `canBeEqual(target, arr)` that determines whether `arr` can be made equal to `target` by reversing the order of the elements. The function takes in two parameters: `target` and `arr`, both lists of non-negative integers that may contain duplicates. The function should return `True` if `arr` can be made equal to `target` after reordering the elements, and `False` otherwise.
"""

from collections import Counter

def canBeEqual(target, arr):
    return Counter(target) == Counter(arr)