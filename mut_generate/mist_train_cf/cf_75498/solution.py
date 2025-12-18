"""
QUESTION:
Create a function `generate_primes(n)` that generates all prime numbers from 1 to `n` (inclusive). The function should return a list of prime numbers. Note that the function should only consider integers.
"""

def generate_primes(n):  
    primes = []
    for potentialPrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(potentialPrime ** 0.5) + 1):
            if potentialPrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(potentialPrime)
    return primes  