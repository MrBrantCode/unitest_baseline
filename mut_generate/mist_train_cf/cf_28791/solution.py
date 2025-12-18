"""
QUESTION:
Create a function named `extract_top_n_words` that takes a multi-line string `disclaimer` and an integer `n` as input. The function should ignore special characters, punctuation, and case sensitivity when counting the words, and return the top `n` most frequently occurring words and their counts.
"""

import re
from collections import Counter

def extract_top_n_words(disclaimer, n):
    """
    Extracts the top n most frequently occurring words from a multi-line string.

    Args:
    disclaimer (str): The input string.
    n (int): The number of top words to return.

    Returns:
    list: A list of tuples containing the top n most frequently occurring words and their counts.
    """
    # Remove special characters and convert to lowercase
    cleaned_disclaimer = re.sub(r'[^a-zA-Z\s]', '', disclaimer).lower()
    # Split the disclaimer into words
    words = cleaned_disclaimer.split()
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Get the top N most common words
    top_n_words = word_counts.most_common(n)
    return top_n_words