"""
QUESTION:
Create a function 'prime_lcm_list' that takes two lists of integers as input: a list of prime numbers and a list of their corresponding counts. The function should return the Least Common Multiple (LCM) of these prime elements raised to their corresponding counts, modulo 10^9 + 7.

The function should be able to handle large inputs and avoid overflow. The input lists are guaranteed to be of the same length, with 1 <= length <= 10^3, and the values in the prime list are between 2 and 10^6, and the values in the count list are between 1 and 10^3.
"""

from typing import List

def prime_lcm_list(primes: List[int], freqs: List[int]) -> int:
    MOD = 10**9 + 7
    ans = 1
    for prime, freq in zip(primes, freqs):
        ans = (ans * pow(prime, freq, MOD)) % MOD
    return ans