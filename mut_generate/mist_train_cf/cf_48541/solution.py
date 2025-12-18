"""
QUESTION:
Write a Python function named `find_element_in_list` that takes two parameters, `element` and `input_list`, where `element` can be of any data type. The function should return the number of occurrences of `element` in `input_list`, which can contain different data types.
"""

def find_element_in_list(element, input_list):
    count = 0
    for i in input_list:
        if i == element:
            count += 1
    return count