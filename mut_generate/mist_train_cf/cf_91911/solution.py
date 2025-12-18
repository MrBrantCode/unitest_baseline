"""
QUESTION:
Write a function called `is_element_present` that takes an array `arr` and an `element` as parameters. The function should return `True` if `element` is found in `arr`, and `False` otherwise. You cannot use any built-in array functions or methods.
"""

def is_element_present(arr, element):
    for num in arr:
        if num == element:
            return True
    return False