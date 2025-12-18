"""
QUESTION:
Create a function named `replace_characters` that takes a string as input. The function should replace each alphabetic character in the string with its next consecutive character, wrapping around from 'z' to 'a' or 'Z' to 'A' when necessary. Non-alphabetic characters should be ignored. The function should handle both uppercase and lowercase letters separately. The input string has a maximum length of 100 characters.
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