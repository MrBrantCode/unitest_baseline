"""
QUESTION:
Write a function named `count_words` that takes a string and an integer as arguments. The function should return the number of words in the string that start with a vowel, end with a consonant, and are of the provided length. The input string can contain multiple sentences and punctuations.
"""

import re

def count_words(string, length):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Split the string into words using regular expression
    words = re.findall(r'\b\w+\b', string.lower())
    
    count = 0
    for word in words:
        if len(word) == length and word[0] in vowels and word[-1] in consonants:
            count += 1
    
    return count