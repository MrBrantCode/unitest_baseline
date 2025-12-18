"""
QUESTION:
Develop a function `top_k_words(text, k)` that identifies the top K most commonly used words in a given text. The function should take two parameters: `text`, the input string, and `k`, the number of top words to return. It should return a list of the K most frequently occurring words in the text, ignoring case and punctuation. The list should be sorted in descending order of frequency.
"""

import re
from collections import Counter

def top_k_words(text, k):
    """
    Identifies the top K most commonly used words in a given text.

    Args:
    text (str): The input string.
    k (int): The number of top words to return.

    Returns:
    list: A list of the K most frequently occurring words in the text, 
          ignoring case and punctuation, sorted in descending order of frequency.
    """
    # Remove punctuations and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split text into individual words
    words = text.split()

    # Count the occurrences of each word
    word_count = Counter(words)

    # Sort the word count dictionary by values in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Get the top K words
    top_k = sorted_words[:k]

    # Return the top K words
    return [word[0] for word in top_k]