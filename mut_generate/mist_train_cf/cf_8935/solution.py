"""
QUESTION:
Create a function `remove_elements` that takes a list `lst` and a value as parameters, and returns a new list with all instances of the given value removed, without using any built-in Python methods or libraries for list modification.
"""

def remove_elements(lst, val):
    new_lst = []
    for element in lst:
        if element != val:
            new_lst.append(element)
    return new_lst