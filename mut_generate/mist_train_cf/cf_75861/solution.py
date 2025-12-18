"""
QUESTION:
Write a function `multiply_numbers` that takes an array of integers as input and returns the product of all numbers in the array that leave a remainder of 1 when divided by 3.
"""

def multiply_numbers(array):
    product = 1
    for number in array:
        if number % 3 == 1:
            product *= number
    return product