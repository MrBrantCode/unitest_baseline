"""
QUESTION:
Create a function `find_palindromes` that takes a string `text` as input and returns a set of unique palindromic words found in the text. The function should ignore case sensitivity, punctuation, and spacing, treating words as if all letters are lowercase without punctuation and spaces in between. The function should be optimized for efficiency to handle large texts.
"""

import re

def find_palindromes(text):
    # initialize an empty set to store the palindrome words
    palindromes = set()

    # split the text into words
    words = text.split()

    # for each word in words
    for word in words:
        # clean the word by removing punctuation and converting to lower case
        cleaned_word = re.sub(r'[^\w\s]','',word).lower()
        # check if the cleaned word is a palindrome
        if cleaned_word == cleaned_word[::-1]:
            # if it is, then add it to our set of palindromes
            palindromes.add(cleaned_word)

    return palindromes