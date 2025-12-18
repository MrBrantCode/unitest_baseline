"""
QUESTION:
Write a function `get_numerical_value(input_string)` that calculates the numerical value of a given string by mapping each letter to a prime number and calculating the product of these prime numbers, ignoring any non-alphabetic characters. The product should be calculated using modular arithmetic with a modulo of 1000000007.
"""

def get_numerical_value(input_string):
    prime_mapping = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
        'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
        'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
    }

    product = 1
    for char in input_string:
        if char.isalpha():
            product *= prime_mapping[char.lower()]

    return product % 1000000007