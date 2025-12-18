"""
QUESTION:
Write a function `word_frequency` that takes a string `text` as input and returns the frequency of individual words in the string and the word(s) with the maximum frequency. The function should be case-insensitive and ignore punctuation. If multiple words have the same maximum frequency, return all of them.
"""

from collections import Counter
import string

def word_frequency(text):
    """
    This function calculates the frequency of individual words in a given string
    and returns the word(s) with the maximum frequency. The function is 
    case-insensitive and ignores punctuation.

    Args:
        text (str): Input string

    Returns:
        tuple: A tuple containing a dictionary of word frequencies and a list of 
        words with the maximum frequency along with the count.
    """
    
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the string into words and count frequency
    words = text.split()
    word_counts = Counter(words)

    # Find the words with maximum frequency
    max_freq_count = max(word_counts.values())
    max_freq_words = [word for word, freq in word_counts.items() if freq == max_freq_count]

    return word_counts, max_freq_words, max_freq_count