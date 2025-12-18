"""
QUESTION:
Write a function `find_prime_numbers` that takes a string as input and returns a list of prime numbers found in the string. The function should extract all sequences of digits from the string, and then identify which of these sequences represent prime numbers.
"""

import re

def find_prime_numbers(string):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = re.findall(r'\b\d+\b', string)  # Extract all numbers from the string
    prime_numbers = []
    for number in numbers:
        if is_prime(int(number)):
            prime_numbers.append(int(number))
    return prime_numbers