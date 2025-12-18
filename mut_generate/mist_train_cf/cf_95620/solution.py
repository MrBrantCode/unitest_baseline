"""
QUESTION:
Write a function `add_next_prime` that takes a list of integers as input, adds the next prime number greater than each element to the corresponding element, and returns the modified list. The function should use a helper function `is_prime` to check if a number is prime, and another helper function `generate_next_prime` to find the next prime number greater than a given number. The `is_prime` function should have a time complexity of O(sqrt(n)) and the overall space complexity of `add_next_prime` should be O(n).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_next_prime(n):
    prime = n + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1

def add_next_prime(lst):
    result = []
    for num in lst:
        prime = generate_next_prime(num)
        result.append(num + prime)
    return result