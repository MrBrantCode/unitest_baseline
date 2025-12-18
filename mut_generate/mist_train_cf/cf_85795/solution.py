"""
QUESTION:
Create a function called 'concatenate_chars' that takes an array of characters as input, concatenates the alphabetic characters into a singular string, and ignores non-alphabetic characters and spaces. The function should handle variable-length input arrays, upper-case and lower-case letters, and return the result as a string without spaces.
"""

def concatenate_chars(char_array):
    result = ''
    for char in char_array:
        if char.isalpha():
            result += char
    return result.replace(' ', '')