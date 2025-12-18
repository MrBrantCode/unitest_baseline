"""
QUESTION:
Implement the `sieve_of_eratosthenes` function to find all prime numbers up to a given limit without using pre-defined functions or libraries. The function should handle a large range of numbers (up to 10^6) efficiently.
"""

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False] # 0 and 1 are not primes
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            # Mark multiples of the current number as False
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False
    primes = [num for num in range(2, limit + 1) if sieve[num]]
    return primes