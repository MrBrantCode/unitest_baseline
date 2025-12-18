"""
QUESTION:
Create a function `find_frequencies(s1, s2)` that takes two strings `s1` and `s2` as input and returns a dictionary containing the frequency of each character that appears in both strings. The frequency of each character in the output dictionary should be the minimum frequency of that character in `s1` and `s2`.
"""

from collections import Counter

def find_frequencies(s1, s2):
    # Create Counter objects for each string
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    # Find the intersection of keys in both Counters
    common_keys = set(counter1.keys()) & set(counter2.keys())

    # Return the frequencies from the intersection set
    return {key: min(counter1[key], counter2[key]) for key in common_keys}