"""
QUESTION:
Write a Python function named `sum_even_numbers_recursive` that takes a list as input and returns the sum of all even numbers in the list. The list may contain negative numbers and the sum can be negative as well. The function should handle nested lists.
"""

def sum_even_numbers_recursive(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += sum_even_numbers_recursive(item)
        elif isinstance(item, int) and item % 2 == 0:
            total += item

    return total