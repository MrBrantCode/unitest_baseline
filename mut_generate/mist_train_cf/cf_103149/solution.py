"""
QUESTION:
Write a function named `check_equal` that takes a list of elements as input and returns True if all elements in the list are equal, regardless of their data types, and False otherwise. The function should also handle the case where the input list is empty.
"""

def check_equal(lst):
    if len(lst) == 0:
        return True
    first_element = lst[0]
    for element in lst:
        if element != first_element:
            return False
    return True