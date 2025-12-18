"""
QUESTION:
Implement a function `sum_even_numbers` that takes a list of integers as input and returns the sum of all the even numbers in the list. The function should not use any conditional statements (if, else) or loops (for, while), and instead utilize Python's built-in higher-order functions and functional programming techniques.
"""

def sum_even_numbers(numbers: list) -> int:
    from functools import reduce
    return reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, numbers), 0)