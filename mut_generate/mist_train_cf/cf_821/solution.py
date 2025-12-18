"""
QUESTION:
Create a function named `count_words` that takes a string and a list of stop words as input, and returns a dictionary with each unique word in the string as a key and its frequency as the value. The function should ignore punctuation and be case insensitive, and remove all stop words from the string before counting the occurrences of each word. The time complexity of the function should be O(n), where n is the length of the string.
"""

import re

def count_words(string, stop_words):
    string = re.sub(r'[^\w\s]', '', string).lower()
    words = string.split()
    words = [word for word in words if word not in stop_words]
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count