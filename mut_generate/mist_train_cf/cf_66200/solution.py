"""
QUESTION:
Write a recursive function `modify_string` that takes a string `s` as input and returns a modified string. Iterate over each character in the string in reverse order, converting vowels to uppercase and consonants to lowercase, while leaving non-alphabet characters unchanged. Do not use standard library functions for identifying vowels or determining case.
"""

def modify_string(s, index=None):
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    consonants_lower = 'bcdfghjklmnpqrstvwxyz'
    consonants_upper = 'BCDFGHJKLMNPQRSTVWXYZ'

    if index is None:
        index = len(s) - 1

    if index < 0:
        return s

    if s[index] in vowels_lower:
        s = s[:index] + s[index].upper() + s[index+1:]
    elif s[index] in vowels_upper:
        s = s[:index] + s[index] + s[index+1:]
    elif s[index] in consonants_lower or s[index] in consonants_upper:
        s = s[:index] + s[index].lower() + s[index+1:]

    return modify_string(s, index - 1)