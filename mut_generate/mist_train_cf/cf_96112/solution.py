"""
QUESTION:
Implement a function `find_suggestions` that provides autocomplete or predictive search feature given a prefix. The function should take in a list of words, their corresponding frequencies, and a prefix as input, and return a list of suggestions based on the prefix. The function should prioritize suggestions based on the frequency of word usage, with more popular words appearing higher in the list, and should have a time complexity of O(log n) or better.
"""

import bisect

def find_suggestions(words, frequencies, prefix):
    """
    Provides autocomplete or predictive search feature given a prefix.
    
    Args:
    words (list): A list of words.
    frequencies (list): A list of frequencies corresponding to the words.
    prefix (str): The prefix to search for in the words.
    
    Returns:
    list: A list of suggestions based on the prefix, prioritized by frequency.
    """
    word_freq = {word: freq for word, freq in zip(words, frequencies)}
    words.sort()
    start = bisect.bisect_left(words, prefix)
    end = bisect.bisect_right(words, prefix + "~")
    suggestions = words[start:end]
    suggestions.sort(key=lambda word: word_freq[word], reverse=True)
    return suggestions