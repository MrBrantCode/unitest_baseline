"""
QUESTION:
Create a function `FrequentStringsInText` that takes a string of continuous characters as input and returns a dictionary where each distinct word corresponds to a key and its frequency of appearance as the value. The function should be case-sensitive, handle common punctuation marks, and disregard them. The function should also achieve optimal performance with a time complexity of O(n), where n is the length of the input string.
"""

import re

def FrequentStringsInText(strInput):
    hashWord = {}
    words = re.findall(r'\b\w+\b', strInput)
    for word in words:
        if word in hashWord:
            hashWord[word] += 1
        else:
            hashWord[word] = 1
    return hashWord