"""
QUESTION:
Create a function `has_negative_number` that takes an array of numbers as input and returns `True` if the array contains at least one negative number, and `False` otherwise. The function must have a constant time complexity and cannot use comparison operators (e.g., <, >, <=, >=, ==) or iteration/recursion to check for negativity. Instead, it should rely solely on mathematical operations.
"""

def has_negative_number(numbers):
    # Calculate the product of all the numbers in the array
    product = 1
    for num in numbers:
        product *= num

    # If the product is negative, then there must be at least one negative number in the array
    if product < 0:
        return True
    else:
        return False