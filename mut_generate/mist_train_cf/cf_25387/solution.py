"""
QUESTION:
Create a function `get_most_used_words` that takes a string as input and returns the top 10 most frequently used words in the string. The function should consider word frequency regardless of case and should treat punctuation as part of the word. The output should be a list of words. The input string may contain multiple spaces between words, but this should not affect the output.
"""

import collections
import re

def get_most_used_words(string):
    # Convert string to lower case and tokenize the string
    words = re.findall(r'\b\w+\b', string.lower())

    # Calculate frequency of each word
    freq = collections.Counter(words)

    # Sort the words in descending order of frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Get the top ten most used words
    most_used_words = [word for word, count in sorted_freq[:10]]

    return most_used_words