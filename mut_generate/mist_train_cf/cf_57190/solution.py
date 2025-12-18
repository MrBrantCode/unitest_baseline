"""
QUESTION:
Create a function named `add_element(element, list_=None)` that takes an element and a list as arguments and returns the list with the element appended to it. The function should handle the case when the list argument is not provided (i.e., it defaults to `None`) and the case when the same list object is passed multiple times to the function. The function should return a new list with the element appended to it each time it is called, without modifying the original list.

Note that the function should avoid the misuse of mutable objects that leads to unexpected behavior when calling the function multiple times with the same list object. The corrected version of the function should create a copy of the original list so that the original list is not changed when a new element is appended to it.
"""

def add_element(element, list_=None):
    if list_ is None:
        list_ = []
    else:
        list_ = list_.copy()  # create a copy of list so original is not modified
    list_.append(element)
    return list_