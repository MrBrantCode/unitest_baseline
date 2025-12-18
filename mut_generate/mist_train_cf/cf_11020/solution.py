"""
QUESTION:
Write a function `contains_element` that checks if a given element exists in an array of integers or floating-point numbers. The array can have a maximum length of 10^6 and the element can be any number between -10^9 and 10^9. The function should return True if the element is found and False otherwise, with a time complexity of O(n), where n is the length of the array.
"""

def contains_element(array, element):
    for item in array:
        if item == element:
            return True
    return False