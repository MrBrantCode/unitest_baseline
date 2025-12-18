"""
QUESTION:
Write a function `largest_prime_factor(n: int)` that returns the largest prime factor of the absolute value of the integer `n`. The function should work for both positive and negative integers and assume that the absolute value of `n` is greater than 1 and is not a prime number.
"""

def largest_prime_factor(n: int):
    n = abs(n)  # to accommodate negative integers, take the absolute value
    i = 2       # start dividing from 2, the smallest prime number
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n