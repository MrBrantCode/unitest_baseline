"""
QUESTION:
Create a function named `word_frequencies` that takes two parameters: a string `text` and a list of `stopwords`. The function should return a dictionary where the keys are individual words from the `text` (excluding the `stopwords`) and the values are their respective frequencies. The function should be case sensitive and consider punctuation as part of a word.
"""

from collections import defaultdict

def word_frequencies(text, stopwords):
    words = text.split()
    freqs = defaultdict(int)
    
    for word in words:
        if word not in stopwords:
            freqs[word] += 1
    return dict(freqs)