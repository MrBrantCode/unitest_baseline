"""
QUESTION:
Write a function `isUgly(num)` that determines whether a given positive integer `num` is an ugly number, where an ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. The function should return `True` if `num` is an ugly number, and `False` otherwise.
"""

def isUgly(num):
    if num <= 0:
        return False  # Negative numbers and zero are not considered ugly numbers

    while num % 2 == 0:
        num = num / 2

    while num % 3 == 0:
        num = num / 3

    while num % 5 == 0:
        num = num / 5

    return num == 1  # If num becomes 1, it means all prime factors are 2, 3, or 5