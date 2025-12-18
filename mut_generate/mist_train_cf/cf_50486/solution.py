"""
QUESTION:
Write a function `largest_prime_factor(n: int)` that returns the largest prime divisor of an integer `n`. The function should handle both positive and negative integers and assume that the absolute value of `n` is greater than 1 and `n` is not a prime number but a power of a prime. The function should not use libraries like 'sympy' or 'numpy'.
"""

def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime divisor of the integer 'n',
    Both positive and negative integers are handled
    Prime factor identification is optimized by checking divisors up to sqrt(n)
    """
    n = abs(n)  
    factor = 2  
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n