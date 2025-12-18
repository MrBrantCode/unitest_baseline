"""
QUESTION:
Compute a hash code for a string using a custom hashing algorithm that takes into account both the characters, the length of the string, and the occurrence of each character in the string. The hash code should be computed using a prime number modulo and the final result should be in a base 16 format. The function should handle string inputs with non-ASCII characters and strings with duplicate characters using the formula `(ASCII value of character * length of string) % prime` when a character occurs more than once.

The function should be named `compute_hash_code` and it should use the prime number 31 for modulo.
"""

def compute_hash_code(string):
    hash_code = 0
    prime = 31  
    length = len(string)
    char_occurrences = {}  

    for char in string:
        if char not in char_occurrences:
            char_occurrences[char] = 1
        else:
            char_occurrences[char] += 1

    for char in string:
        if char_occurrences[char] > 1:
            hash_code += (ord(char) * length) % prime
        else:
            hash_code += ord(char)

    hash_code = hash_code % prime
    return hex(hash_code)[2:]