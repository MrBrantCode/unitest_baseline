"""
QUESTION:
Write a Python program that contains two functions: `is_prime(n)` and `main()`. The `is_prime(n)` function checks if a number `n` is prime and returns a boolean value. It should only check for divisibility up to the square root of `n`. The `main()` function should prompt the user to enter a number `n`, then print all prime numbers from 1 to `n` separated by semicolons, and also print the count of composite numbers within this range.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True