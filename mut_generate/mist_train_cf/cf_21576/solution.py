"""
QUESTION:
Create a function named `find_first_non_consonant_vowel` that takes a string as input and returns the index position of the first vowel that is not immediately followed by a consonant. The function should return -1 if no such vowel is found.
"""

def find_first_non_consonant_vowel(string):
    vowels = "aeiou"
    i = 0
    while i < len(string):
        if string[i] in vowels:
            if i+1 >= len(string) or string[i+1] in vowels:
                return i
        i += 1
    return -1