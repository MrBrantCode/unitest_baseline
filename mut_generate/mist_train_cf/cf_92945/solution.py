"""
QUESTION:
Create a function `find_first_vowel(string)` that takes a string as input and returns the index of the first vowel that is not immediately followed by another vowel. If no such vowel is found, the function should return -1. Vowels are defined as 'a', 'e', 'i', 'o', and 'u', and the function should be case-insensitive.
"""

def find_first_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i].lower() in vowels:
            if i + 1 < len(string) and string[i + 1].lower() not in vowels:
                return i
            elif i + 1 == len(string):
                return i
    return -1  # Return -1 if no vowel found