"""
QUESTION:
Write a function `generate_squared_primes(number)` that generates a list of numbers that are the squares of all prime numbers between 1 and the given number, with a time complexity of O(n*sqrt(k)), where n is the given number and k is the largest prime number between 1 and n.
"""

import math

def generate_squared_primes(number):
    primes = []
    for i in range(1, number+1):
        if i >= 2 and all(i % j != 0 for j in range(2, int(math.sqrt(i))+1)):
            primes.append(i * i)
    return primes