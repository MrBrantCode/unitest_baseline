"""
QUESTION:
Create a function called `count_unique_words` that takes a string of text as input. The function should return the count of unique words in the text, excluding common stop words, with a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the number of unique words in the string. The input string contains only alphabetic characters, spaces, and punctuation marks. The function should handle consecutive multiple spaces and punctuation marks, and ignore common stop words like "the", "and", "a".
"""

import re

def count_unique_words(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    unique_words = set()
    stop_words = set(['the', 'and', 'a'])
    for word in words:
        if word not in stop_words:
            unique_words.add(word)
    return len(unique_words)