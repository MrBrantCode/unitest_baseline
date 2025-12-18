"""
QUESTION:
Write a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function must have a time complexity of O(n).
"""

def pairs_sum_to_zero(lst):
    """Checks if there are two distinct elements in the list that sum to zero."""
    set_lst = set(lst)
    for num in set_lst:
        if -num in set_lst and num != 0 or -num != num:
            return True
    return False