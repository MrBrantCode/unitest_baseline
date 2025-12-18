"""
ORIGINAL QUESTION:
Create a function `calculate_numbers(n)` that takes a positive integer `n` as input and returns the cumulative total of its digits and the sum of the factorials of its digits. The function should raise an error or return an error message if `n` is not a positive integer.
"""

import math

def calculate_numbers(n):
    # Check if input is positive integer
    if not isinstance(n, int) or n <= 0:
        return "Input should be a positive integer"
  
    # Convert number to list of digits
    digits = [int(x) for x in str(n)]
  
    # Calculate cumulative total of digits
    total = sum(digits)
  
    # Calculate sum of factorials of digits
    factorial_sum = sum(math.factorial(i) for i in digits)
  
    return total, factorial_sum