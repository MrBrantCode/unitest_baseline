"""
QUESTION:
Replace every occurrence of 'a' with 'b' in the input string and return the resulting string if it is a palindrome, contains exactly 3 vowels in ascending alphabetical order, and has a length that is a prime number. If no such string can be found after replacing all 'a's with 'b's, return None.
"""

import string

def entrance(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    string = s.replace('a', 'b')

    if string == string[::-1] and len([c for c in string if c in vowels]) == 3:
        vowel_indices = [i for i, c in enumerate(string) if c in vowels]
        vowel_chars = [string[i] for i in vowel_indices]

        if vowel_chars == sorted(vowel_chars) and len(string) in primes:
            return string

    return None