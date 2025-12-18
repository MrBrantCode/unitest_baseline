"""
QUESTION:
Create a function named `prime_lcm_list` that takes two input lists of integers: `primes` containing prime numbers and `freqs` containing their corresponding counts. The function should calculate the Least Common Multiple (LCM) of the prime numbers raised to their counts and return the result modulo 10^9 + 7. 

Constraints: The input lists should have the same length between 1 and 10^3, each prime number should be between 2 and 10^6, and each count should be between 1 and 10^3.
"""

from typing import List

def prime_lcm_list(primes: List[int], freqs: List[int]) -> int:
    mod = 10**9 + 7 # Avoid overflow by using modulo
    lcm = 1
    for prime, freq in zip(primes, freqs):
        lcm = (lcm * pow(prime, freq, mod)) % mod
    return lcm