"""
QUESTION:
Write a function called `find_lexemes` that takes a sentence and a character set as input, and returns a list of words from the sentence that start with the given character set. The search should be case-sensitive and ignore standalone punctuation marks.
"""

import string

def find_lexemes(sentence, start):
    # Remove punctuation but leave words with punctuation within them
    words = [''.join([char for char in word if char not in string.punctuation]) 
             for word in sentence.split()]
    # Filter words starting with "start"
    result = [word for word in words if word.startswith(start)]
    return result