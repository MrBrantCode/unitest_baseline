"""
QUESTION:
Write a function named `sort_string` that takes a string containing several words as input. The function should convert all words to lowercase, remove any words that contain numbers or special characters, and remove any duplicate words. Then, it should sort the remaining words in descending order based on the length of each word. The function should not use any built-in sorting or data structure functions and should be able to handle input strings of up to 10^6 characters efficiently, without causing memory or performance issues.
"""

import re

def sort_string(string):
    string = string.lower()
    words = string.split()
    words = [word for word in words if re.match('^[a-zA-Z]+$', word)]
    words = list(set(words))
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(words[j]) < len(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return ' '.join(words)