"""
QUESTION:
Write a function called `longest_word(s)` that takes a string `s` as input and returns the longest word in the string. The string may contain multiple words separated by spaces and/or punctuation.
"""

def longest_word(s):
    words = s.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()
    max_length = 0
    longest_word = ''
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word