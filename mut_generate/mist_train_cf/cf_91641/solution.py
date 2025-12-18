"""
QUESTION:
Write a function named `contains_element` that checks whether an array of integers or floating-point numbers contains a given element. The function should return True if the element is found and False otherwise. The array length is limited to 10^6 elements, and the element can be any number between -10^9 and 10^9. The function must have a time complexity of O(n), where n is the length of the array.
"""

def contains_element(array, element):
    for item in array:
        if item == element:
            return True
    return False