"""
QUESTION:
Write a function `product_of_numbers_with_modulus_one` that takes a list of integers as input. The function should return the product of all numbers in the list that leave a remainder of 1 when divided by 3.
"""

def product_of_numbers_with_modulus_one(numbers):
    """Returns the product of all numbers in the list that leave a remainder of 1 when divided by 3."""
    result = 1
    for number in numbers:
        if number % 3 == 1:
            result *= number
    return result