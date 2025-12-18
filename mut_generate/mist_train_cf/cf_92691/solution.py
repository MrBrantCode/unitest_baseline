"""
QUESTION:
Create a function `get_cumulative_primes` that takes a list of integers as input and returns a list of length 10. The returned list should contain the cumulative sum of the input list, but only include the cumulative sum if it is a prime number. If the number of cumulative prime sums is less than 10, append zeros to reach a length of 10.
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

def get_cumulative_primes(given_list):
    cumulative_primes = []
    cumulative_sum = 0

    for num in given_list:
        cumulative_sum += num
        if is_prime(cumulative_sum):
            cumulative_primes.append(cumulative_sum)

    while len(cumulative_primes) < 10:
        cumulative_primes.append(0)

    return cumulative_primes