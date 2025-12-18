"""
QUESTION:
Write a function named `find_longest_word` that takes a JSON string as input, where the keys in the JSON object are strings. The function should return the longest word (key) in the JSON object and a dictionary containing the count of each character in the longest word. If there are multiple words with the same maximum length, the function should return the first one encountered.
"""

import json

def find_longest_word(json_string):
    data = json.loads(json_string)
    words = list(data.keys())
    longest_word = max(words, key=len)
    char_counts = {}
    for char in longest_word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return longest_word, char_counts