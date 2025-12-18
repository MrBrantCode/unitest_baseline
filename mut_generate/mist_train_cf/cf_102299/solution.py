"""
QUESTION:
Write a function named `count_words_with_vowel` that takes a string as input and returns two values: the number of words that contain at least one vowel, and the length of the longest word that contains at least one vowel. The input string may contain special characters and punctuation marks.
"""

import re

def count_words_with_vowel(string):
    words = string.split()
    count = 0
    longest_length = 0
    
    for word in words:
        if re.search('[aeiouAEIOU]', word):
            count += 1
            if len(word) > longest_length:
                longest_length = len(word)
    
    return count, longest_length