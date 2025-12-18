"""
QUESTION:
Create a function `generate_prime_numbers(start, end)` that generates and returns a list of prime numbers within the given range, inclusive of the end value. The function should start checking from 2 if the start value is less than 2. Implement an optimized algorithm that checks for prime numbers by only iterating up to the square root of the number.
"""

import math

def generate_prime_numbers(start, end):
    primes = []
    for num in range(max(2, start), end+1):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
           primes.append(num)
    return primes