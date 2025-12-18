"""
QUESTION:
Design a function 'prime_lcm_list' that takes two lists of integers as input - a list of distinct prime numbers and a list of corresponding positive frequencies - and returns the Least Common Multiple (LCM) of these prime factors raised to their respective frequencies modulo 10^9 + 7. The function should handle lists of lengths up to 10^3, prime numbers up to 10^6, and frequencies up to 10^3.
"""

from typing import List

def prime_lcm_list(primes: List[int], freqs: List[int]) -> int:
    MOD = 10**9 + 7
    result = 1
    for prime, freq in zip(primes, freqs):
        result = (result * pow(prime, freq, MOD)) % MOD
    return result