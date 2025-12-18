"""
QUESTION:
Create a function named `filter_and_sort` that accepts an array of strings. The function should filter out the strings that do not contain prime numbers and sort the remaining strings based on the smallest prime number contained in each string from smallest to largest.
"""

import re

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_and_sort(strings):
    str_dict = {}
    for string in strings:
        numbers = re.findall('\d+', string)
        primes = [int(num) for num in numbers if is_prime(int(num))]
        if primes:
            str_dict[string] = min(primes)
    sorted_strings = sorted(str_dict, key=str_dict.get)
    return sorted_strings