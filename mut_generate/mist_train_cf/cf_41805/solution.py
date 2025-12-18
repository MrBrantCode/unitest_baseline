"""
QUESTION:
Given a positive integer `n`, write a function `sum_of_odd_digits_squares(n)` that calculates the sum of the squares of all the odd digits in the binary representation of `n`. The function should take in a positive integer `n` and return the sum of the squares of the odd digits in the binary representation of `n`. The binary digit is considered odd if the digit itself is 1.
"""

def sum_of_odd_digits_squares(n: int) -> int:
    result = 0
    while n > 0:
        if n & 1 == 1:
            result += 1  # Add the square of the odd digit
        n >>= 1  # Right shift to consider the next bit
    return result