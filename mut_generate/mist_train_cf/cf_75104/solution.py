"""
QUESTION:
Design a function `product_of_digits` that takes a positive integer as input, calculates the product of its non-zero digits, and returns the result. The function should be able to handle input integers up to 20 digits long and ignore trailing zeros. Assume the input is a non-negative integer without leading zeros, and note that the function does not perform any input validation.
"""

def product_of_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        if digit != 0:
            product *= digit
        num = num // 10
    return product