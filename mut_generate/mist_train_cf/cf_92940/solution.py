"""
QUESTION:
Write a function `replace_consonants` that takes a string as input and returns a new string where each consonant character is replaced with the next character in the alphabet, while ignoring vowels and considering 'z' and 'Z' as exceptions that wrap around to 'a' and 'A' respectively.
"""

def replace_consonants(string):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in string:
        if char.isalpha() and char not in vowels:
            if char.lower() == 'z':
                result += 'a' if char.islower() else 'A'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char
    return result