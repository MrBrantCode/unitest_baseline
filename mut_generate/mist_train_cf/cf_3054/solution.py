"""
QUESTION:
Write a function `contains_element(arr, element)` that checks if a given array `arr` contains a specific `element`. The array can contain integers or floating-point numbers, and the element can be any number between -10^15 and 10^15. The function should return `True` if the element is found and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).
"""

def contains_element(arr, element):
    for num in arr:
        if num == element:
            return True
    return False