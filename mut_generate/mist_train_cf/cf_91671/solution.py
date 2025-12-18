"""
QUESTION:
Compose a function `find_prime_chars(stringA, stringB)` that takes two strings as input. The function should return an array of characters that are in `stringA` and are also prime numbers (i.e., their ASCII values are prime numbers). Ignore `stringB` in the computation.
"""

def find_prime_chars(stringA, stringB):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Find characters that are in stringA and are prime numbers
    prime_chars = []
    for char in stringA:
        if char.isalpha() and ord(char.lower()) in primes:
            prime_chars.append(char)
    
    return prime_chars