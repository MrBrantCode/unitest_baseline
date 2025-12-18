"""
QUESTION:
Write a function `first_n_elements_reversed` that takes a list and an integer `n` as parameters and returns the first `n` elements of the list in reverse order. If the list is `None`, not a list, or its length is less than `n`, the function should raise an exception.
"""

def first_n_elements_reversed(lst, n):
    if lst is None:
        raise Exception("list is null or undefined")
    if not isinstance(lst, list):
        raise Exception("input is not a list") 
    if len(lst) < n:
        raise Exception("list length is less than N")
    return lst[:n][::-1]