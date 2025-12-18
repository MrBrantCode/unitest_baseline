"""
QUESTION:
Create a function named `extract_and_count_words` that takes a string as input and returns a list of tuples. The function should extract all words from the input string using regex, convert them to uppercase, count the frequency of each word, and sort them in descending order of their frequency. The output list of tuples should contain each word and its corresponding frequency.
"""

import re
from collections import Counter

def extract_and_count_words(input_string):
    """
    Extract all words from the input string using regex, convert them to uppercase, 
    count the frequency of each word, and sort them in descending order of their frequency.

    Args:
        input_string (str): The input string from which words will be extracted.

    Returns:
        list: A list of tuples containing each word and its corresponding frequency.
    """

    # Extract words using regex
    words = re.findall(r'\b\w+\b', input_string)

    # Convert to uppercase
    words_uppercase = [word.upper() for word in words]

    # Count the frequency of each word
    word_frequency = Counter(words_uppercase)

    # Sort words in descending order of frequency
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_words