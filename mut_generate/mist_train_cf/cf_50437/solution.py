"""
QUESTION:
Create a function named `find_perfect_squares(start, end)` that takes two integers `start` and `end` as input. The function should return a dictionary where the keys are perfect squares between `start` and `end` (inclusive), and the values are boolean values indicating whether the square root of each perfect square is a prime number (True) or not (False).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_perfect_squares(start, end):
    squares = {}
    for number in range(start, end + 1):
        sqrt = math.sqrt(number)
        if sqrt.is_integer():
            squares[number] = is_prime(sqrt)
    return squares