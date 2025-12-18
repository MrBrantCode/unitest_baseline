"""
QUESTION:
Develop a function named `lcm_primes` that calculates the least common multiple of all prime numbers within a given boundary. The function should take an integer `boundary` as input, representing the upper limit for the numbers to be considered, and return the least common multiple of all prime numbers within that boundary.
"""

def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def lcm_primes(boundary):
    lcm = 1
    for i in range(2, boundary+1):
        if is_prime(i):
            lcm *= i
    return lcm