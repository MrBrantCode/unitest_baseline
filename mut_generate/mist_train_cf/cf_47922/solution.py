"""
QUESTION:
Write a function called `sum_of_squares` that calculates the sum of the squares of all prime numbers within a given range, inclusive of the upper limit. The function should take two parameters, `lower` and `upper`, which define the range of numbers to check.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def sum_of_squares(lower, upper):
    """Calculate the sum of squares of all primes in a given range."""
    sum_squares = 0
    for i in range(lower, upper + 1):
        if is_prime(i):
            sum_squares += i ** 2
    return sum_squares