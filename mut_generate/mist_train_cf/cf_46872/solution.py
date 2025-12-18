"""
QUESTION:
Design a function `count_pairs` that calculates the frequency of all unique pairs of characters in a given text string. The function should handle special characters and numbers, and treat pairs as distinct based on character order (e.g., 'ab' and 'ba' are considered different pairs).
"""

import collections
import itertools

def count_pairs(text):
    # Convert the text string to a list of characters
    chars = list(text)
    
    # Get all unique pairs of characters
    pairs = list(itertools.combinations(chars, 2))
    
    # Count the frequency of each pair
    pair_frequencies = collections.Counter(pairs)
    
    return pair_frequencies