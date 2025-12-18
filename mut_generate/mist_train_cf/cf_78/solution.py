"""
QUESTION:
Write a Python function named `sum_even_numbers` that takes a list as input, which may contain integers and nested lists, and returns the sum of all even numbers in the list and its nested lists. The function should handle negative numbers and the possibility of a negative sum. Implement this function using recursion.
"""

def sum_even_numbers(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_even_numbers(item)
        elif isinstance(item, int) and item % 2 == 0:
            total += item
    return total