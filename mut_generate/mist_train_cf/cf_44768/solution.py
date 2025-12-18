"""
QUESTION:
Create a function `generate_primes(n)` that generates a sequence of prime numbers up to a specified number `n` in ascending order. The function should only include real prime numbers and should be efficient for large values of `n`.
"""

def generate_primes(n):
    # Initialize a list to indicate whether each number 2 through N is prime.
    # Initially, we assume that all are prime.
    is_prime = [True] * (n+1)
    p = 2

    # Update 'is_prime' for all multiples of each found prime
    while p**2 <= n:
        if is_prime[p]:  # if 'p' is prime
            for i in range(p**2, n+1, p):
                is_prime[i] = False
        p += 1
    
    # Generate the list of primes
    prime_numbers = [p for p in range(2, n+1) if is_prime[p]]

    return prime_numbers