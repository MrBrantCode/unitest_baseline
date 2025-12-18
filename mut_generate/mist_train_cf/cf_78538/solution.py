"""
QUESTION:
Create a function named `reverse_string_and_count` that takes a string `s` as input and returns the reversed string along with the count of vowels and consonants. The function should be case-insensitive and ignore non-alphabet characters such as digits, spaces, and special characters. The input string can contain uppercase and lowercase letters, numbers, and special characters.
"""

def reverse_string_and_count(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    s = s.lower()
    reversed_s = s[::-1]

    vowel_count = 0
    consonant_count = 0

    for char in reversed_s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return reversed_s, vowel_count, consonant_count