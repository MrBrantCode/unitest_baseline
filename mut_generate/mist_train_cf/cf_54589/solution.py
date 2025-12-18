"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and should not check for divisors beyond the square root of `n`.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        square_root_n = int(n**0.5) + 1
        for i in range(3, square_root_n, 2):
            if n % i == 0:
                return False
        return True