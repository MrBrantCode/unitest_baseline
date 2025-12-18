"""
QUESTION:
Write a function named `contains_element` that checks if an element is present in a given array. The array can contain integers or floating-point numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the array, which can be up to 10^9. The element can be any number between -10^15 and 10^15.
"""

def contains_element(arr, element):
    for num in arr:
        if num == element:
            return True
    return False