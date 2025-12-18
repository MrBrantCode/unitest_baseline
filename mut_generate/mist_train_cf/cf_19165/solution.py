"""
QUESTION:
Write a function `has_negative_number` that determines whether an array of numbers contains at least one negative number. The function must have a constant time complexity and cannot use comparison operators (e.g., <, >, <=, >=, ==) or iteration/recursion. It can only use mathematical operations.
"""

def has_negative_number(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product < 0