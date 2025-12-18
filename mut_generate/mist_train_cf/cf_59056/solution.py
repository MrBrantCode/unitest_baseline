"""
QUESTION:
Write a function `pig_latin` that takes a word as input and converts it to Pig Latin, preserving the original capitalization and punctuation. If the word starts with one or more consonants, move them to the end of the word and append "ay". If the word ends with punctuation, keep the punctuation at the end after conversion. The word should start with uppercase.
"""

import string

def pig_latin(word):
    """
    Convert a word to Pig Latin
    """
    vowels = "aeiou"
    word = word.lower()
    punct_end = ""

    # Check if the word ends with a punctuation
    for char in string.punctuation:
        if word.endswith(char):
            word = word[:-1]
            punct_end = char

    # Move initial consonants to the end of the word and add "ay"
    while word and word[0] not in vowels:
        word = word[1:] + word[0]

    return word.capitalize() + "ay" + punct_end