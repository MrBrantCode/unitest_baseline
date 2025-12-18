"""
QUESTION:
Write a function called `remove_even_numbers` that takes an array of numbers as input and returns the array with all even numbers removed. The function should use the built-in `filter` function to achieve this.
"""

def remove_even_numbers(array):
    return list(filter(lambda x: x % 2 != 0, array))