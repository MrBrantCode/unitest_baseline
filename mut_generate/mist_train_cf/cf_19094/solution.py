"""
QUESTION:
Write a function `longest_unique_word(words)` that takes a list of words as input and returns the longest word that contains only unique characters. If there are multiple words with the same length and unique characters, return the word that appears first in the list. If the input list is empty or all words have duplicate characters, return an empty string.
"""

def longest_unique_word(words):
    if len(words) == 0:
        return ""

    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            if len(set(word)) == len(word):
                longest_word = word
                max_length = len(word)

    return longest_word