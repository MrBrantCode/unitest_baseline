"""
QUESTION:
Write a function called `modify_terminal_item` that takes a numpy array as input, accesses its last element (regardless of the number of dimensions), and modifies it to a specified new value.
"""

import numpy as np

def modify_terminal_item(array, new_value):
    array[-1] = new_value
    return array