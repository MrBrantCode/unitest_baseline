"""
QUESTION:
Write a function named `find_most_frequent_word` that takes a string `text` as input, containing up to 1000 words, and returns the most frequently used word in the text, ignoring common stop words ("is", "a", "of", "and", "in") and punctuation, and treating the text as case-insensitive.
"""

from collections import Counter
import re

def find_most_frequent_word(text):
    stop_words = ['is', 'a', 'of', 'and', 'in']  # common stop words

    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Split text into individual words
    words = cleaned_text.split()

    # Remove stop words
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word
    word_count = Counter(words)

    # Find the most frequently used word
    most_frequent_word = word_count.most_common(1)[0][0]

    return most_frequent_word