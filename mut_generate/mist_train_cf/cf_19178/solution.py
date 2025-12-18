"""
QUESTION:
Write a function named `count_letters` that takes a string as input and returns a dictionary containing the count of each unique alphabet (both uppercase and lowercase) in the string. The function should ignore any non-alphabet characters such as punctuation marks, special characters, and spaces, and consider uppercase and lowercase letters as separate entities. The function should only consider the English alphabet.
"""

import string

def count_letters(input_string):
    alphabet = string.ascii_lowercase
    count = {}

    for char in input_string:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count