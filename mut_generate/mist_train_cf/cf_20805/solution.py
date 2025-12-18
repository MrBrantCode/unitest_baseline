"""
QUESTION:
Write a function `get_top_ten_most_used_words` that takes a string as input, returns the top ten most frequently occurring words excluding any words that contain numbers or special characters, and runs in O(n log n) time complexity where n is the number of words in the string. The input string can contain up to 100,000 characters and the words can have a maximum length of 50 characters.
"""

import re
from collections import Counter

def get_top_ten_most_used_words(string):
    """
    Returns the top ten most frequently occurring words excluding any words that contain numbers or special characters.

    Args:
        string (str): The input string.

    Returns:
        list: A list of the top ten most used words.
    """

    # Split the string into individual words
    words = string.split()

    # Filter out words containing numbers or special characters
    filtered_words = [word for word in words if not re.search('[^a-zA-Z]', word)]

    # Count the frequency of each word
    word_freq = Counter(filtered_words)

    # Sort the dictionary by values in descending order and extract the top ten most used words
    top_ten_words = [word for word, freq in word_freq.most_common(10)]

    return top_ten_words