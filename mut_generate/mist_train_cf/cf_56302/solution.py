"""
QUESTION:
Write a function named `count_prime_numbers` that takes a string `s` as input and returns the count of occurrences of prime number digits (2, 3, 5, and 7) in the string. The function should be case sensitive and consider only the specified prime number digits.
"""

import re 

def count_prime_numbers(s):
    # find the occurrence of prime number digits and return the length
    return len(re.findall('[2357]', s))