"""
QUESTION:
Create a function called `remove_vowels` that takes a string `s` as input and returns a new string with all vowels (both uppercase and lowercase) removed from `s`. The function should not modify the original string.
"""

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    s_without_vowels = ''
    for char in s:
        if char not in vowels:
            s_without_vowels += char
    return s_without_vowels