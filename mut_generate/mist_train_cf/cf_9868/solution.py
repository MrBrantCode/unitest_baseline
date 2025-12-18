"""
QUESTION:
Create a function named `count_unique_words` that takes a sentence and a set of stopwords as input and returns the number of unique words in the sentence excluding the stopwords. The function should ignore case, handle punctuation marks and special characters, and have a time complexity of O(n), where n is the length of the sentence.
"""

import string

def count_unique_words(sentence, stopwords):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.lower().split()
    unique_words = set()
    for word in words:
        if word not in stopwords:
            unique_words.add(word)
    return len(unique_words)