"""
QUESTION:
Write a function `shift_letters` that takes a string of characters as input and returns a new string where each letter in the input string is replaced by its immediate successor in the English alphabet, wrapping around from 'z' to 'a' and from 'Z' to 'A', while leaving non-alphabetic characters unchanged.
"""

def shift_letters(text):
    result = ""
    for char in text:
        if char.isalpha():
            # Start with Z or z for looping the alphabet
            if char.lower() == 'z':
                result += 'a' if char.islower() else 'A'
            else: 
                result += chr(ord(char) + 1)
        else:
            result += char

    return result