"""
QUESTION:
Create a function `top_words` that takes a list of strings and an optional integer `n` as input. The function should return a dictionary with the unique words from the strings as keys and their frequency of appearance as values, ignoring case sensitivity. If `n` is provided, the function should return the top `n` words based on their frequency; otherwise, it should return the dictionary for all words.
"""

import collections
import itertools

def top_words(lst: list, n=None):
    words = list(itertools.chain(*[s.lower().split() for s in lst]))
    freq_dict = collections.Counter(words)
    
    if n is not None:
        freq_dict = dict(freq_dict.most_common(n))
      
    return freq_dict