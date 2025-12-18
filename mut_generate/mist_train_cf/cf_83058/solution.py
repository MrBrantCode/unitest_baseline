"""
QUESTION:
Write a Python function named `replace_vowels_with_underscore` that takes a string as input and returns the string with all vowel characters replaced with underscores. The function should handle both lowercase and uppercase vowels.
"""

def replace_vowels_with_underscore(string):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        string = string.replace(vowel, '_')
    return string