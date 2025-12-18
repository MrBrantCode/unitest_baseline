"""
QUESTION:
Find the time and space complexity of a function `prime_factors(n)` that takes a positive integer `n` and returns a list of its prime factors. The function should iterate from 2 to the square root of `n` and use an inner loop to check for divisibility. Assume that the input `n` is a positive integer and optimize by iterating only up to the square root of `n`.
"""

def prime_factors(n):
    """
    This function takes a positive integer n and returns a list of its prime factors.
    
    The function iterates from 2 to the square root of n and uses an inner loop to check for divisibility.
    
    Parameters:
    n (int): A positive integer.
    
    Returns:
    list: A list of prime factors of the given number.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors