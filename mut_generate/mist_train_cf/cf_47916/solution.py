"""
QUESTION:
Create a function named `prime_information` that takes an integer `n` as input and returns two outputs:

- A dictionary where the keys are prime numbers between 2 and `n-1` (inclusive) and the values represent the frequency of each prime number.
- A list of prime gaps, where a prime gap is defined as the difference between two consecutive prime numbers.

Restrictions:

- The function should be optimized to handle larger numerical spectrums efficiently.
- The input `n` should be a positive integer greater than 2.
- The output dictionary keys should be unique prime numbers and their corresponding values should be 1, since prime numbers are unique.
- The output list of prime gaps should contain the differences between consecutive prime numbers in the spectrum.
"""

def prime_information(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if (primes[p] == True):
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = {}
    prime_gaps = []
    last_prime = None
    for p in range(2, n):
        if primes[p]:
            prime_numbers[p] = 1
            if last_prime:
                prime_gaps.append(p-last_prime)
            last_prime = p

    return prime_numbers, prime_gaps