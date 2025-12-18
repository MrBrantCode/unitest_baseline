"""
QUESTION:
Create a function `check_prime(n)` that takes a single integer argument `n` and returns a boolean indicating whether `n` is a prime number or not. The function should be efficient and not check divisibility beyond the square root of `n`.
"""

def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True