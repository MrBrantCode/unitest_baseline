"""
QUESTION:
Create a function called `generate_prime_pairs` that takes a list of numbers as input and returns all possible pairs of numbers from the list where the sum of each pair is a prime number. The function should consider each pair only once, i.e., it should not include both (a, b) and (b, a) if a and b are different numbers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_pairs(nums):
    prime_pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if is_prime(nums[i] + nums[j]):
                prime_pairs.append((nums[i], nums[j]))
    return prime_pairs