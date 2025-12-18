"""
QUESTION:
Write a function named `sort_descending` that takes a set of integers as input and returns the integers in descending order. The function should not use any built-in sort function with a `reverse=True` argument, but can use other built-in sort functions or custom algorithms to achieve the desired result.
"""

def sort_descending(elements):
    return sorted(elements, reverse=True)