"""
QUESTION:
Write a function named `get_last_element` that takes a deque as input and returns the last element. The function should utilize Python's standard library and support deques of any size. The deque can contain elements of any data type.
"""

from collections import deque

def get_last_element(d):
    return d[-1]