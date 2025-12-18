"""
QUESTION:
Write a function named `longest_word_length` that takes a string `s` as input and returns the length of the longest word in the string. The string is split into words by spaces, and punctuation is not considered part of a word.
"""

def longest_word_length(s):
    words = s.split(' ')
    return max(len(word.strip('.,!?"\'').lower()) for word in words)