"""
QUESTION:
Find the maximum prime number in the given array and its index after removing any duplicates. 

The function `find_max_prime(numbers)` should accept a list of integers `numbers` as input. It should return a string with the maximum prime number and its index in the format "The maximum prime number is [prime number] at index [index]". If the array does not contain any prime numbers, the function should return "Error: No prime numbers found in the array."
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime(numbers):
    seen = set()
    primes = []
    for num in numbers:
        if is_prime(num) and num not in seen:
            seen.add(num)
            primes.append(num)
    if not primes:
        return "Error: No prime numbers found in the array."
    max_prime = max(primes)
    max_index = primes.index(max_prime)
    return f"The maximum prime number is {max_prime} at index {max_index}."