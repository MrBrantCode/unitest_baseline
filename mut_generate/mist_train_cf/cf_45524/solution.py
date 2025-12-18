"""
QUESTION:
Create a function `lexical_frequency` that takes a string `text` as input, filters out non-letter characters, splits the string into individual lexical terms, counts the frequency of each term, and returns a dictionary where the key is the lexical term and the value is its frequency. The dictionary should maintain the order of the terms as they appeared in the original string.
"""

import re
from collections import OrderedDict

def lexical_frequency(text):
    # Split the text into words and strip out non-letters
    terms = re.findall(r'\b\w+\b', re.sub(r'[^A-Za-z\s]', '', text))
    
    # Use an ordered dict to retain the order of terms in the string
    term_freq = OrderedDict()

    # Count the frequency of each term
    for term in terms:
        if term in term_freq:
            term_freq[term] += 1
        else:
            term_freq[term] = 1

    return term_freq