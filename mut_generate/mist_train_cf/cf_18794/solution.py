"""
QUESTION:
Create a function `deduct_if_conditions_met` that takes an integer as input and returns the integer with 10 deducted if it meets the following conditions: the number is greater than 100, it is divisible by 5, and it is not a prime number. If the conditions are not met, the function should return the original integer.
"""

def deduct_if_conditions_met(n):
    """Deduct 10 from the input number if it is greater than 100, divisible by 5, and not a prime number."""
    return n - 10 if n > 100 and n % 5 == 0 and not all(n % i != 0 for i in range(2, int(n**0.5)+1)) else n