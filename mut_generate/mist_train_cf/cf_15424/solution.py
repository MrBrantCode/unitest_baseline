"""
QUESTION:
Create a function named `extract_and_count_unique_words` that takes a sentence as input, extracts unique words (excluding common stop words and punctuation marks), and returns a dictionary containing the unique words and their frequencies. The function should handle sentences with words in different cases (uppercase and lowercase) and exclude common stop words such as "the", "and", "a", etc. from the final list of unique words.
"""

import string
from collections import Counter

def extract_and_count_unique_words(sentence):
    """
    Extract unique words from a sentence, count their frequency, and exclude common stop words.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary containing unique words and their frequencies.
    """
    # Convert sentence to lowercase and remove punctuation marks
    sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Split sentence into words
    words = sentence.split()
    
    # Define common stop words
    stop_words = ['the', 'and', 'a', 'an', 'in', 'of', 'to', 'is', 'are']
    
    # Filter out stop words and count the frequency of each word
    word_count = Counter(word for word in words if word not in stop_words)
    
    return dict(word_count)