"""
QUESTION:
Create a function `find_first_vowel(string)` that finds the index of the first vowel in a given string `string` that is not immediately followed by a consonant. The function should return the index of the first such vowel, or -1 if no such vowel is found. The search should be case-insensitive.
"""

def find_first_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i].lower() in vowels:
            if i + 1 < len(string) and string[i + 1].lower() not in vowels:
                return i
            elif i + 1 == len(string):
                return i
    return -1