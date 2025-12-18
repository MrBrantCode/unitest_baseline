"""
QUESTION:
Write a function called `process_string` that takes a string input, reverses it, converts it to uppercase, removes any non-alphabetic characters (including digits, special characters, and punctuation marks), and handles Unicode characters. The function should return the resulting string. The function should be able to handle any type of character, including Unicode characters, and should normalize them to their closest ASCII representation if necessary.
"""

import unicodedata 

def process_string(input_string):
    input_string = unicodedata.normalize('NFD', input_string)
    reversed_string = input_string[::-1]
    upper_string = reversed_string.upper()
    final_string = ''.join(e for e in upper_string if e.isalpha())
    return final_string