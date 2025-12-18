"""
QUESTION:
Create a function called `has_recurring_elements` that takes an array as input and returns `True` if the array contains any recurring elements and `False` otherwise. The function should be able to handle arrays containing elements of any data type.
"""

def has_recurring_elements(arr):
    element_set = set()

    for element in arr:
        if element in element_set:
            return True
        element_set.add(element)

    return False