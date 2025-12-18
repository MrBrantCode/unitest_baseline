"""
QUESTION:
Create a function named `count_lowercase_consonants` that takes a string `s` as input and returns the total count of lowercase consonants present in the string. The function should only consider the English alphabets and ignore any other characters, including uppercase letters and non-alphabets.
"""

def count_lowercase_consonants(s):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return sum(1 for char in s if char in consonants)