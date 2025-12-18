"""
QUESTION:
Implement a function `check_even(arr)` that checks if all elements in the list are even numbers. The function should return `True` if all elements are even integers, `False` if not all elements are even integers, "The list is empty" if the list is empty, and "The list contains a mix of integers and strings" if the list contains a mix of integers and strings. The list may contain integers and/or strings.
"""

def check_even(arr):
    if not arr:
        return "The list is empty"
    elif all(isinstance(x, int) for x in arr):
        return all(x % 2 == 0 for x in arr)
    else:
        return "The list contains a mix of integers and strings"