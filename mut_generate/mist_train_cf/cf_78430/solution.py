"""
QUESTION:
Write a function named `get_primes_and_gaps` that takes an integer `n` as input, where `n` is the upper limit of the numerical range, and returns two values: 
- A dictionary where the keys are the prime numbers in the range 1 to `n-1` and the values are their frequencies.
- A list of prime gaps, where a prime gap of length `n` is a run of `n-1` consecutive composite numbers between two successive prime numbers.
 
The function should be optimized to perform efficiently for larger ranges.
"""

def get_primes_and_gaps(n):
    sieve = [True] * (n + 1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for i in range(x*x, n + 1, x): 
                sieve[i] = False
    primes = [x for x in range(2, n) if sieve[x]]
    prime_dict = {p: 1 for p in primes}
    gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]
    return prime_dict, gaps