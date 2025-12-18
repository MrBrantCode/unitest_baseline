"""
QUESTION:
Create a function `check_perfect_square(n)` that takes an integer `n` as input and checks whether it is a perfect square. If `n` is a perfect square, the function should also check whether its square root is a prime number. The function should return a string indicating whether `n` is not a perfect square, a perfect square with a non-prime square root, or a perfect square with a prime square root. The function should be efficient and have a good runtime for large numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_perfect_square(n):
    root = math.sqrt(n)

    if int(root + 0.5) ** 2 == n:
        if is_prime(root):
            return "The number is a perfect square and its square root is a prime number."
        else:
            return "The number is a perfect square but its square root is not a prime number."
    else:
        return "The number is not a perfect square."