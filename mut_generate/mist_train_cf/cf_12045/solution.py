"""
QUESTION:
Create a function called `join_strings_with_vowels` that takes an array of strings as input. The function should concatenate the strings that start with a vowel (a, e, i, o, u) and return the result as a single string. The function should be case-insensitive when checking for vowels and should not include any extra spaces at the end of the result.
"""

def entance(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    
    for string in arr:
        if string[0].lower() in vowels:
            result += string + ' '
    
    return result.strip()