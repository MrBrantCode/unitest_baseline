"""
QUESTION:
Create a function `find_max_prime(numbers)` that takes a list of integers as input, removes any duplicate prime numbers, and returns a string in the format "The maximum prime number is [max_prime] at index [max_index]." where [max_prime] is the maximum prime number and [max_index] is its index in the list of unique primes. If the input list does not contain any prime numbers, return "Error: No prime numbers found in the array."
"""

import math

def find_max_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

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