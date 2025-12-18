"""
QUESTION:
Write a function named `check_strings` that takes a list of strings as input and returns `True` if any string in the list starts with 't' and ends with 'd', has a length that is a prime number, and its middle character is a vowel.
"""

import math

def check_strings(lst):
    vowels = ['a', 'e', 'i', 'o', 'u']

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for word in lst:
        if word.startswith('t') and word.endswith('d'):
            length = len(word)
            if is_prime(length):
                middle_char = word[length // 2]
                if middle_char.lower() in vowels:
                    return True
    return False