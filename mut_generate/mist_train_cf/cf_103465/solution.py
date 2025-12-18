"""
QUESTION:
Write a function named `access_third_element` that takes a list as an argument and returns the third element of the list, assuming the list contains only unique values and has at least three elements, using list comprehension. The function should not modify the original list.
"""

def access_third_element(lst):
    return [x for i, x in enumerate(lst) if i == 2][0]