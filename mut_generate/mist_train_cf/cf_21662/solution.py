"""
QUESTION:
Create a function called `generate_sequence` that takes two integers `k` and `n` as input, where `k` is the starting number and `n` is the ending number. This function should return two lists: one containing a sequence of integers starting at `k` and ending at `n` with each number raised to the power of 1, 2, and 3, and another list containing the prime numbers found within the generated sequence. The function should check for prime numbers efficiently to ensure the overall time complexity is optimized.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_sequence(k, n):
    sequence = []
    primes = []

    for i in range(k, n + 1):
        sequence.append(i)
        sequence.append(i ** 2)
        sequence.append(i ** 3)
        
        if is_prime(i):
            primes.append(i)
    
    return sequence, primes