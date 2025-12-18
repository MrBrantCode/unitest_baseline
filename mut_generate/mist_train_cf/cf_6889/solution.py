"""
QUESTION:
Write a function called `clean_string` that takes a string as input, removes all punctuation marks from the string, converts it to uppercase, and returns a dictionary where the keys are the letters in the string and the values are their respective counts.
"""

import string

def clean_string(str):
    str = str.translate(str.maketrans('', '', string.punctuation))
    str = str.upper()
    letter_counts = {}
    for letter in str:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts