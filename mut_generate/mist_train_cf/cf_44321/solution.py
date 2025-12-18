"""
QUESTION:
Write a function called `odd_numbers` that takes a list of integers as input and returns a list of the odd integers. The function should handle exceptions for non-integer inputs by returning an error message, and it should be able to handle large lists efficiently.
"""

def odd_numbers(lst):
    # Check input types
    if not all(isinstance(i, int) for i in lst):
        return "Error: All elements in the list should be integers."

    # Filter and return odd numbers
    return [i for i in lst if i%2 == 1]