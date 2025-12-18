"""
QUESTION:
Write a function `find_longest_word` that takes a string as input, ignores any punctuation marks, and returns the longest word in the string while accounting for multiple occurrences of the same word and special characters such as emojis or accented characters. The function should have a time complexity of O(n), where n is the length of the string.
"""

import re
from collections import defaultdict

def find_longest_word(string):
    word_count = defaultdict(int)
    longest_word = ""
    words = re.findall(r'\b\w+\b', string, re.UNICODE)  # find all words in the string
    
    for word in words:
        word_count[word] += 1
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word