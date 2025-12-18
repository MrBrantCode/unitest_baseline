"""
QUESTION:
Write a function `word_frequency` that takes a narrative prose as input, scans the prose for unique terms, and returns a dictionary where the keys are the unique terms and the values are their frequencies. The function should ignore case differences and consider 'The' and 'the' as the same word. The function should use regular expressions for scanning and compilation.
"""

import re
from collections import Counter

def word_frequency(prose):
    """
    This function scans a narrative prose for unique terms and returns a dictionary 
    where the keys are the unique terms and the values are their frequencies.

    Args:
        prose (str): A narrative prose.

    Returns:
        dict: A dictionary with unique terms as keys and their frequencies as values.
    """
    words = re.findall(r'\b\w+\b', prose.lower())
    frequency = Counter(words)
    return dict(frequency)