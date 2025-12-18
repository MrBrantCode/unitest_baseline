"""
QUESTION:
Create a function named `generate_primes(start, end)` that generates a list of all prime numbers between a given start and end number, inclusive. The start and end numbers can be as large as 10^6. The function should have a time complexity of O(n√m), where n is the number of prime numbers between the start and end, and m is the average value of those prime numbers.
"""

import math

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes