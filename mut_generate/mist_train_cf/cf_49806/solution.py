"""
QUESTION:
Implement a function `get_longest_word(input_string)` that takes an arbitrary string as input, splits it into individual words, and returns the longest word. The function should return the first word with the maximum length if there are multiple words with the same maximum length.
"""

def get_longest_word(input_string):
    words = input_string.split(" ")
    longest_word = max(words, key=len)
    return longest_word