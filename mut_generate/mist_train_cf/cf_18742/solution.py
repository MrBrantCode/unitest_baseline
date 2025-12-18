"""
QUESTION:
Create a function called `get_numerical_value` that calculates the numerical value of a given string by mapping each letter to a prime number and summing these prime numbers. The sum should be calculated using modular arithmetic with a modulo of 1000000007. Ignore non-alphabetic characters in the string.
"""

def get_numerical_value(string):
    primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    total = 0
    
    for char in string:
        if char.isalpha():
            total += primes[char.lower()]
    
    return total % 1000000007