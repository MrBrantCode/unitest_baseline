"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that generates a list of prime numbers between 2 and a given positive integer `n` (greater than 2) using the Sieve of Eratosthenes algorithm. The function should return a list of integers representing the prime numbers in the specified range.
"""

def sieve_of_eratosthenes(n):
    # Create a list of boolean values representing whether each number is prime
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    # Iterate through all numbers up to square root of n
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Mark all multiples of i as non-prime
            for j in range(i*i, n+1, i):
                primes[j] = False

    # Generate the list of prime numbers
    prime_numbers = [i for i in range(2, n+1) if primes[i]]
    return prime_numbers