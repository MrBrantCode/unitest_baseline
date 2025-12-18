"""
QUESTION:
Write a function `singleton_pos` that takes a list of integers as input and returns a list of indices of the elements that appear only once in the list. The function should be efficient for large lists, i.e., its time complexity should be linear, O(n).
"""

from collections import Counter

def singleton_pos(arr):
    """
    Returns a list of indices of the elements that appear only once in the list.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    list: A list of indices of singleton elements.
    """
    counts = Counter(arr)
    return [i for i, num in enumerate(arr) if counts[num] == 1]