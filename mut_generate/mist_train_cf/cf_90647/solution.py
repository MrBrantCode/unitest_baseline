"""
QUESTION:
Write a function `remove_elements(lst, value)` that takes a list `lst` and a value `value` as parameters. The function should return a new list containing all elements from `lst` except for those equal to `value`. The function must not use any built-in Python methods or libraries.
"""

def remove_elements(lst, value):
    new_lst = []
    for element in lst:
        if element != value:
            new_lst.append(element)
    return new_lst