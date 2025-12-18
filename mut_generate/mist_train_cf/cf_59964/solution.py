"""
QUESTION:
Create a function `is_armstrong(n)` that takes an integer `n` as input and returns a boolean indicating whether it is an Armstrong number. An Armstrong number is equal to the sum of its digits raised to the power of the number of digits.
"""

def is_armstrong(n):
    n = str(n)
    length = len(n)
    return sum(int(digit) ** length for digit in n) == int(n)