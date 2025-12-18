"""
QUESTION:
Write a function `is_cons` that checks if the character at index `i` in the string `string` is a consonant and returns a specific value based on the result. The function should be used in the context of a program that processes a string of characters in a specific language and sets corresponding flags based on the presence of certain patterns in the string. The function should return a value that can be compared to 2 for the purpose of setting a flag `syll.asp` to indicate the presence of a specific type of consonant pattern.
"""

def is_cons(string, i, c):
    cons = 'bcdfghjklmnpqrstvwxyz'
    cons += cons.upper()
    if i < len(string) and string[i] in cons and string[i] not in c:
        return 2
    return 0