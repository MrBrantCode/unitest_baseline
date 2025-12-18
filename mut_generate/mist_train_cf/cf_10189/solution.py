"""
QUESTION:
Create a function `replace_vowels(s)` that takes a string `s` as input and returns a new string where all vowels ('a', 'e', 'i', 'o', 'u' and their uppercase counterparts) are replaced with '*'. The function should work efficiently for strings of up to 10^5 characters.
"""

def replace_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in s:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result