"""
QUESTION:
Implement a function named `get_primes` that takes an integer `n` as input, representing the upper limit, and returns a list of all prime numbers within this limit using the Sieve of Eratosthenes algorithm. The function should exclude non-prime numbers (0 and 1) from the output.
"""

def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers
    for current_prime in range(2, int(n**0.5) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime**2, n + 1, current_prime):
                sieve[multiple] = False
    return [num for num in range(2, n + 1) if sieve[num]]