"""
QUESTION:
Given a list of words, write a function `longest_unique_word` that returns the longest word with only unique characters. If there are multiple words with the same length and unique characters, return the first occurrence in the list. If the input list is empty or all words contain duplicate characters, return an empty string.
"""

def longest_unique_word(words):
    # Return an empty string if the input list is empty
    if len(words) == 0:
        return ""

    longest_word = ""
    max_length = 0

    for word in words:
        # Check if the word is longer than the current longest word
        if len(word) > max_length:
            # Check if the word contains only unique characters
            if len(set(word)) == len(word):
                longest_word = word
                max_length = len(word)

    return longest_word