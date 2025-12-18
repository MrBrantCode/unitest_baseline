"""
QUESTION:
Write a function named `contains_element` that checks if a given element is present in an array of integers or floating-point numbers. The function must return True if the element is found and False otherwise. The function should operate within a time complexity of O(n), where n is the length of the array, and a space complexity of O(1). The array can have a maximum length of 10^7 and the element can be any number between -10^10 and 10^10.
"""

def contains_element(arr, element):
    for num in arr:
        if num == element:
            return True
    return False