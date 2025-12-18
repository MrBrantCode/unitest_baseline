"""
QUESTION:
Create a function `replace_characters` that takes a string of up to 100 characters as input and returns a new string where all alphabetic characters are replaced with the next consecutive letter in the alphabet, wrapping around from 'z' to 'a' or 'Z' to 'A' when necessary, while ignoring non-alphabetic characters.
"""

def replace_characters(string):
    result = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result