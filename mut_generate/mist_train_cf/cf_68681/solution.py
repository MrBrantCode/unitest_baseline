"""
QUESTION:
Create a function called `extract_primes` that takes a dictionary as input. The function should iterate through the dictionary, check if the integer keys or values are prime, and if the sum of ASCII values of string values is prime. It should then return a new dictionary with the same keys as the original dictionary but only including the keys where the value is prime or the sum of the ASCII values is prime. The function should handle both integer and string values in the dictionary.
"""

import math

def extract_primes(input_dict):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def ascii_sum(s):
        return sum([ord(c) for c in s])

    new_dict = {}

    for key, value in input_dict.items():
        if type(value) == int and is_prime(value):
            new_dict[key] = value
        elif type(value) == str:
            sum_ascii = ascii_sum(value)
            if is_prime(sum_ascii):
                new_dict[key] = sum_ascii

    return new_dict