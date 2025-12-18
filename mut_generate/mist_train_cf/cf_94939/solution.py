"""
QUESTION:
Write a function `contains_element(arr, element)` that checks if an array `arr` contains a given numerical `element`. The function should return `True` if the `element` is found in `arr` and `False` otherwise.

The input array `arr` has a maximum length of 10^7 and contains integers or floating-point numbers. The `element` can be any number between -10^10 and 10^10. Implement the function with a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).
"""

def contains_element(arr, element):
    for num in arr:
        if num == element:
            return True
    return False