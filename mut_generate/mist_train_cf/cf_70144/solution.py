"""
QUESTION:
Create a function `is_armstrong(n)` to check if a given number `n` is an Armstrong number, where an Armstrong number is defined as a number where the sum of its individual digits, each elevated to the power equivalent to the total count of digits, is equal to the number itself. The function should return a boolean value. The input number `n` should be a non-negative integer.
"""

def is_armstrong(n):
    power = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** power
    return total == n