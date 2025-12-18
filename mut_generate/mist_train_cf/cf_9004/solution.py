"""
QUESTION:
Write a function `remove_oldest_elements` that takes a list as input and returns the list with its oldest elements removed until the list contains at most 100 elements. The function should preserve the order of the remaining elements.
"""

def remove_oldest_elements(input_list):
    if len(input_list) > 100:
        return input_list[-100:]
    else:
        return input_list