"""
QUESTION:
Write a function named `count_vowels` that takes a string of alphabetic symbols as input and returns the count of vowel phonemes in the string. The function should consider both lowercase and uppercase vowels as valid.
"""

def count_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count