"""
QUESTION:
Write a function named `most_frequent_word` that takes a string as input and returns the most frequently occurring word with a length greater than three. The function should ignore punctuation and be case insensitive. The input string can contain any printable ASCII characters and its length can be up to 10^9 characters. The function should have a time complexity of O(n), where n is the length of the input string, and should be optimized for memory usage.
"""

import re

def most_frequent_word(string):
    string = re.sub(r'[^\w\s]', '', string)
    words = string.lower().split()
    word_count = {}
    for word in words:
        if len(word) > 3:  
            word_count[word] = word_count.get(word, 0) + 1
    max_count = 0
    most_frequent = None
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_frequent = word
    return most_frequent