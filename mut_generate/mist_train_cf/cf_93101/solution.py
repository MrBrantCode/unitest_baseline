"""
QUESTION:
Write a function `find_prime_numbers` that takes a string as input, extracts all numbers from the string, checks each number for primality, and returns a list of the prime numbers found. The function should be able to identify prime numbers within non-numeric strings. The numbers in the string may not be separated by spaces or any specific delimiter, but they should be separated from other non-numeric characters.
"""

import re

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(s):
    numbers = re.findall(r'\d+', s)  # Extract all numbers from the string
    return [int(num) for num in numbers if is_prime(int(num))]