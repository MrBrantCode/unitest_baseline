"""
QUESTION:
Write a function `largest_prime_factor(n)` that takes in an integer `n` and returns the largest prime factor of `n`. If the input number `n` is less than 2, the function should return 0.
"""

def largest_prime_factor(n):
    if n < 2:
        return 0

    # Remove all the factors of 2
    while n % 2 == 0:
        n = n // 2

    # After removing all factors of 2, the largest prime factor will be odd
    largest_factor = 1
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n = n // i

    # If the remaining number is a prime number greater than 2, it is the largest prime factor
    if n > 2:
        largest_factor = n

    return largest_factor