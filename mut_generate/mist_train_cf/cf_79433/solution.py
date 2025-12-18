"""
QUESTION:
Write a function called `word_frequency` that takes two parameters: a list of sentences and a list of stopwords. The function should return a dictionary where the keys are unique words (case-insensitive) across all sentences, excluding stopwords and punctuation marks, and the values are the number of occurrences of each word.
"""

from collections import Counter
import string

def word_frequency(sentences, stopwords):
    words = []
    # Convert list of sentences to list of words
    for sentence in sentences:
        for word in sentence.split():
            # Remove punctuation from the end of each word
            word = word.strip(string.punctuation)
            # Convert to lower case
            word = word.lower()
            # Exclude stopwords
            if word not in stopwords:
                words.append(word)
    # Count word occurrence
    word_count = Counter(words)
    return dict(word_count)