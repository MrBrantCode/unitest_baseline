"""
QUESTION:
Create a function `fib_primes(n)` that generates a Fibonacci sequence where all elements are prime numbers up to the nth term. The function should have a time complexity under O(n^2) and a space complexity under O(n).
"""

import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    
    # 0 and 1 are not prime numbers
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True
    
    # all other even numbers are not primes
    if n % 2 == 0:
        return False

    max_divisor = math.isqrt(n)  # Check divisibility up to the square root of n
    for d in range(3, 1 + max_divisor, 2):  
        if n % d == 0:
            return False
    return True


def fib_primes(n):
    """Generate Fibonacci sequence of prime numbers up to n-th term."""
    
    primes = []
    fib_seq = [0, 1]
  
    while len(primes) < n:
        f = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(f)

        if is_prime(f):
            primes.append(f)
  
    return primes