"""
QUESTION:
Write a function named `sum_of_digits` that takes a string of digits as input, calculates the sum of its digits, ignoring any leading zeros, and returns the result. The input string can be up to 1000 characters long and represents a positive integer.
"""

def sum_of_digits(n):
    # Ignore leading zeros
    n = str(n).lstrip('0')
    
    # Calculate sum of digits
    digit_sum = sum(map(int, str(n)))
    
    return digit_sum