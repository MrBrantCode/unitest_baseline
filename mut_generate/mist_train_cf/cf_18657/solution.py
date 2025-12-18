"""
QUESTION:
Write a function `element_present(arr, element)` that checks if `element` is present in the array `arr` using a single loop and without using any built-in array functions or methods. The function should return `True` if `element` is found and `False` otherwise.
"""

def entrance(arr, element):
    for i in arr:
        if i == element:
            return True
    return False