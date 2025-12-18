"""
QUESTION:
Write a function `is_recursive` that takes a function as an argument and returns `True` if the function is recursive (i.e., it calls itself) and `False` otherwise. Assume the input function is a simple recursive function with a single method call to itself. The solution should be implemented in Python and may not be 100% reliable, but should work for simple cases.
"""

def is_recursive(func):
    return func.__code__.co_name in func.__code__.co_names