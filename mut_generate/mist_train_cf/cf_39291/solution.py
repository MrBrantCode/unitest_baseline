"""
QUESTION:
Write a function `filter_none_elements` that takes a tuple as input and returns a new tuple containing only the non-None elements of the input tuple, preserving their original order. The input tuple contains elements of various types including None and has a length between 1 and 100.
"""

def filter_none_elements(input_tuple):
    return tuple(x for x in input_tuple if x is not None)