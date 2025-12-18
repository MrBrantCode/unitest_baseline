"""
QUESTION:
Write a recursive function `product_of_digits(n)` that calculates the product of all non-zero digits in a given integer `n`. The function should exclude any zeros present in the number and return the product of the remaining digits.
"""

def product_of_digits(n):
    # Base case: when n reduce to 0, return 1
    if n == 0:
        return 1

    # Extract the last digit 
    digit = n % 10
    
    # Call the function again with the remaining digits
    remaining = n // 10

    # If the digit is not 0, multiply it with the result from the remaining digits
    if digit != 0:
        return digit * product_of_digits(remaining)
    else: # else, just return the result from the remaining digits
        return product_of_digits(remaining)