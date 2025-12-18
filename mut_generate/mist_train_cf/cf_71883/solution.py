"""
QUESTION:
Create a function `generate_cryptogram(sentence)` that replaces each letter in the given sentence with a different letter that has a prime ASCII value, while maintaining the frequency count of each letter. The function should only substitute alphabetic characters and keep non-alphabetic characters unchanged. The replacement letters should be chosen from the set of ASCII characters (both uppercase and lowercase) with prime ASCII values.
"""

import string

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_cryptogram(sentence):
    ascii_primes = [char for char in string.ascii_letters if is_prime(ord(char))]
    
    substitutions = {}
    cryptogram = ''
    
    for char in sentence:
        if char.isalpha():
            if char not in substitutions:
                substitutions[char] = ascii_primes.pop(0)
            cryptogram += substitutions[char]
        else:
            cryptogram += char
            
    return cryptogram