"""
QUESTION:
Create a function `count_and_locate_keywords(text, keywords)` that takes a string `text` and a list of keywords as input, and returns two dictionaries: one containing the positions of each keyword occurrence in the string, and another containing the count of occurrences for each keyword. The function should be case-insensitive and ignore special characters. The position count should start from 1.
"""

import re

def count_and_locate_keywords(text, keywords):
    text = text.lower()
    words = text.split()
    dict_keywords = {keyword.lower(): [] for keyword in keywords}
    for i, word in enumerate(words):
        clean_word = re.sub(r'\W+', '', word)
        if clean_word in dict_keywords:
            dict_keywords[clean_word].append(i+1)
    dict_count = {key: len(value) for key, value in dict_keywords.items()}
    return dict_keywords, dict_count