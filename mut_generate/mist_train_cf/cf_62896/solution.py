"""
QUESTION:
Implement a function `count_prime_digits` that takes an integer `number` (0 ≤ |number| ≤ 10^12) and returns the total number of prime digits (2, 3, 5, or 7) in the given number.
"""

def count_prime_digits(number: int) -> int:
    prime_digits = {"2", "3", "5", "7"}
    return sum(digit in prime_digits for digit in str(abs(number)))