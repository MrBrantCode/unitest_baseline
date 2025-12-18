"""
QUESTION:
Write a function named `prime_factors(n)` that finds and returns all prime factors of a given number `n`. The function should be efficient, with a time complexity of O(sqrt(N)) where N is the given number.
"""

def prime_factors(n):
    factors = []
    
    # Check for divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for divisibility by 3
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    
    # Check for divisibility by other odd primes
    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            factors.append(i)
            n = n // i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n = n // (i + 2)
            
    # If n is a prime greater than 2
    if n > 2:
        factors.append(n)
    
    return factors