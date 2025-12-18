"""
QUESTION:
Write a function `count_letters(input_string)` that counts the number of unique English alphabets in a given string, ignoring punctuation marks, special characters, and spaces. The function should handle both uppercase and lowercase letters and return a dictionary containing the count of each unique letter. The function should only consider English alphabets.
"""

import string

def count_letters(input_string):
    alphabet = string.ascii_lowercase
    count = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count