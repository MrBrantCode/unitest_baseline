"""
QUESTION:
Generate a function `generate_fibonacci` that creates a Fibonacci sequence up to the sum of the first 5 prime numbers between two given numbers. The function should take no arguments. The Fibonacci sequence should start with 0 and 1, and each subsequent number should be the sum of the previous two. The sum of the first 5 prime numbers should be calculated between 10 and 100. The function should return the generated Fibonacci sequence.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_primes(start, end):
    primes = []
    current_number = start
    while len(primes) < 5:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1
    return sum(primes)

def generate_fibonacci():
    n = sum_primes(10, 100)
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence