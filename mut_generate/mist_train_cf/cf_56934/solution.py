"""
QUESTION:
Design a function called `count_elements` that takes a nested list as input, where the depth of nesting can be arbitrary, and returns the total number of elements in the list. The function should be able to handle lists within lists.
"""

def count_elements(nested_list):
    count = 0
    for element in nested_list:
        if type(element) == list:
            count += count_elements(element)
        else:
            count += 1
    return count