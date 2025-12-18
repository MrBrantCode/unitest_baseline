"""
QUESTION:
Write a function named `longest_word(sentence)` that takes a string `sentence` as input and returns the longest word without any duplicate letters or the letter 'e'. The function should ignore punctuation marks within the sentence by treating them as part of the word.
"""

import string

def longest_word(sentence):
    words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
    longest = ""
    longest_length = 0
    
    for word in words:
        if len(set(word)) == len(word) and 'e' not in word:
            if len(word) > longest_length:
                longest = word
                longest_length = len(word)
    
    return longest