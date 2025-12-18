"""
QUESTION:
Write a function `count_word_occurrences` that takes a string `comment_block` as input and returns a dictionary where the keys are the unique words found in the comment block and the values are the counts of each word. The function should ignore any non-alphabetic characters, consider words in a case-insensitive manner, and define a word as a sequence of alphabetic characters separated by non-alphabetic characters or the beginning/end of the comment block.
"""

import re

def count_word_occurrences(comment_block):
    words = re.findall(r'\b\w+\b', comment_block.lower())
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count