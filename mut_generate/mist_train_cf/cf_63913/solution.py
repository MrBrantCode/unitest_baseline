"""
QUESTION:
Create a function called `reverse_list` that takes a list of integers as input and returns the list in reverse order without using built-in functions like `reverse()` or slicing. The function should handle lists of any length.
"""

def reverse_list(items):
    reversed_items = [0]*len(items)

    for i in range(len(items)):
        reversed_items[i] = items[len(items) - i - 1]

    return reversed_items