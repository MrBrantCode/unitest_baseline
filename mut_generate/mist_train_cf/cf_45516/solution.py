"""
QUESTION:
Write a function `standardize_case(phrase)` that takes a string `phrase` as input and returns a string with each word's casing standardized according to the following rules: words at even positions are transformed to uppercase and words at odd positions are transformed to lowercase, considering the phrase to be zero-indexed. The function should also strip any leading and trailing special characters from each word, while keeping internal punctuation. The solution should have a time complexity of O(n), where n is the total number of characters in the string.
"""

import string

def standardize_case(s):
    words = s.split() 
    words = [word.strip(string.punctuation) for word in words]

    for i in range(len(words)):
        if i%2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)