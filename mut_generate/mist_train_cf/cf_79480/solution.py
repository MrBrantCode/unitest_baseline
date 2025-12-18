"""
QUESTION:
Construct a function called `k_frequent_chars` that takes a string `s` and an integer `k` as input, and returns a dictionary containing the k most frequent characters in `s` along with their corresponding frequencies. If there are multiple characters with the same frequency, they should be returned in the order of their appearance in the string. The function should only consider unique characters and their frequencies.
"""

from collections import Counter

def k_frequent_chars(s, k):
    # construct a dictionary with character frequencies
    freq_dict = dict(Counter(s))

    # list containing the sorted keys of the dictionary above by their corresponding values  
    sorted_keys = sorted(freq_dict, key=freq_dict.get, reverse=True)
    
    # return top k frequent characters and their frequencies
    return {key: freq_dict[key] for key in sorted_keys[:k]}