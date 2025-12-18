"""
QUESTION:
Create a function named `count_words` that takes two parameters: a string and a list of stop words. The function should return a dictionary where each unique word from the string is a key, and the number of times it appears in the string is the value. The function should ignore punctuation and be case insensitive, and it should exclude the given stop words from the word count. The time complexity of the function should be O(n), where n is the length of the string.
"""

import re

def count_words(string, stop_words):
    string = re.sub(r'[^\w\s]', '', string).lower()
    words = [word for word in string.split() if word not in stop_words]
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count