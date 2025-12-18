"""
QUESTION:
Create a function called `generate_prime_sum_pairs` that takes a list of numbers as input and returns all possible pairs of unique numbers from the list where the sum of each pair is both a prime number and a perfect square number. The pairs should be sorted in ascending order.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return root * root == num

def generate_prime_sum_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            if is_prime(pair_sum) and is_perfect_square(pair_sum):
                pairs.append((numbers[i], numbers[j]))
    
    pairs.sort()
    return pairs