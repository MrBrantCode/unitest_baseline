"""
QUESTION:
Write a function `calculate_sum_of_digits` that takes three integers `x`, `y`, and `z` as input, calculates the product of these integers, and returns the sum of the digits of the product.
"""

def calculate_sum_of_digits(x, y, z):
    product = x * y * z
    sum_of_digits = 0
    
    # Converting the product to a string to iterate over its digits
    product_string = str(product)
    
    # Calculating the sum of the digits
    for digit in product_string:
        sum_of_digits += int(digit)
    
    return sum_of_digits