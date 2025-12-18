"""
QUESTION:
Write a function `is_prime(n)` that takes a number `n` as input, returns a tuple containing a boolean indicating whether the number is prime and the number of factors `n` has. The function should return the result directly without printing it. The input number `n` will always be a positive integer.
"""

def is_prime(n):
    if n < 2:
        return (False, 0)
    else:
        factors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                factors += 1
        if factors == 2:
            return (True, factors)
        else:
            return (False, factors)