"""
QUESTION:
Create a function named `count_vowels` that takes a string `s` as input and returns a dictionary with each vowel ('a', 'e', 'i', 'o', 'u', 'y') as a key and their respective frequency in the string as the value. The count should be case-insensitive.
"""

def count_vowels(s):
    vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
    for char in s.lower():
        if char in vowels_count.keys():
            vowels_count[char] += 1
    return vowels_count