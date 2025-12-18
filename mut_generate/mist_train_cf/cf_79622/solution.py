"""
QUESTION:
Create a function `is_perfect(n)` that determines if a given positive integer `n` is a perfect number. A perfect number is equal to the sum of its positive divisors, excluding the number itself. The function should return `True` if `n` is a perfect number and `False` otherwise. The input `n` is an integer and the function should handle cases where `n` is less than 1.
"""

def is_perfect(n):
    if n < 1:
        return False

    perfect_sum = 0
    for i in range(1, n):
        if n % i == 0:
            perfect_sum += i

    return perfect_sum == n