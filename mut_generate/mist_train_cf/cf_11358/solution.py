"""
QUESTION:
Write a function `count_unique_words` that takes a string of text as input, disregards any punctuation marks, and considers words in a case-insensitive manner. The function should return the number of unique words in the text. The input text may contain leading or trailing whitespaces around words.
"""

import string

def count_unique_words(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    words = text.lower().split()
    unique_words = {}
    for word in words:
        word = word.strip()
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1
    return len(unique_words)