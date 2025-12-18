"""
QUESTION:
Implement a function `primes(limit)` that generates a list of all prime numbers less than the given non-negative integer `limit`. If the limit is 0 or 1, return an empty list.
"""

def entrance(limit):
    if limit < 2:
        return []
    
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime
    
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit, num):
                sieve[multiple] = False
    
    return [num for num, is_prime in enumerate(sieve) if is_prime]