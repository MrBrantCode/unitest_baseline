"""
QUESTION:
Implement a function `count_words(input_str, stop_words)` that takes a string of words `input_str` and a list of stop words `stop_words` as input. Return a tuple containing the total count of non-stop words and a dictionary with the frequency of each non-stop word in descending order of frequency. The function should consider only alphanumeric words (ignoring punctuation, case, and word boundaries). The input string may contain multiple spaces, tabs, or newline characters between words.
"""

from collections import Counter
import re

def count_words(input_str, stop_words):
    """
    Counts the total number of non-stop words and returns a dictionary with the frequency of each non-stop word.

    Args:
        input_str (str): A string of words.
        stop_words (list): A list of stop words.

    Returns:
        tuple: A tuple containing the total count of non-stop words and a dictionary with the frequency of each non-stop word in descending order of frequency.
    """
    # Split the string into words
    words = re.findall(r'\b\w+\b', input_str)

    # Filter out the stop words
    non_stop_words = [word.lower() for word in words if word.lower() not in stop_words]

    # Count the frequency of non-stop words
    word_count = dict(Counter(non_stop_words))

    # Sort the dictionary by value in descending order
    word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    
    return len(non_stop_words), word_count