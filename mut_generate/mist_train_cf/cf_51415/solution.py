"""
QUESTION:
Create a function `remove_vowels` that takes a string `s` as input and returns the string with all vowels removed. The function should handle edge cases such as empty strings and spaces, and maintain consistent capitalization by preserving the original case of non-vowel characters.
"""

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    if not s:
        return s
    return "".join(c for c in s if c not in vowels)