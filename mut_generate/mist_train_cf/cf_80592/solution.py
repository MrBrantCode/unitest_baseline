"""
QUESTION:
Write a recursive function `highest_prime(n, i=2)` that finds the highest prime divisor of a given number `n`. The function should start checking for divisors from `i`, which defaults to 2. The function should handle cases where `n` is 2 or less and return the highest prime divisor. If no prime divisor is found, return -1.
"""

def highest_prime(n, i=2):
    if n <= 2:
        if n == 2:
            return n
        else:
            return -1

    if n % i == 0:
        n = n / i
        if n == 1:
            return i
        else:
            return highest_prime(n, i)
    else:
        return highest_prime(n, i + 1)