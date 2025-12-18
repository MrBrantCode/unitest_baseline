"""
QUESTION:
Create a function `prime_lcm_list_modinv` that receives three inputs: a list of prime numbers, a list of their corresponding frequencies, and an integer `x`. The function should return the Least Common Multiple (LCM) of these prime factors raised to their respective frequencies, multiplied by the modular inverse of `x`, and then taken modulo 10^9 + 7. The modular inverse of `x` should be calculated efficiently.

Constraints:
- The lengths of the lists of prime numbers and frequencies are equal and range from 1 to 10^3.
- Prime numbers range from 2 to 10^6.
- Frequencies range from 1 to 10^3.
- `x` ranges from 1 to 10^9.
"""

from typing import List

MOD = 10**9 + 7  # define the modulo value

def prime_lcm_list_modinv(primes: List[int], freqs: List[int], x: int) -> int:
    lcm = 1
    # LCM of prime factors raised to their respective frequencies
    for prime, freq in zip(primes, freqs):
        lcm = (lcm * pow(prime, freq, MOD)) % MOD
    # multiply LCM with modular inverse of 'x'
    result = (lcm * pow(x, MOD-2, MOD)) % MOD
    return result