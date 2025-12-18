"""
QUESTION:
Create a function named `char_frequency_and_first_unique` that takes a string `s` as input. The function should return a dictionary with two keys: `first_unique_char_index` and `frequency_dist`. The `first_unique_char_index` key should map to the index of the first character in the string that appears only once, treating all characters as lowercase. The `frequency_dist` key should map to a list of tuples, where each tuple contains a character from the input string and its frequency, sorted in increasing order by character.
"""

from collections import Counter, OrderedDict

def char_frequency_and_first_unique(s):
    # convert string to lowercase
    s = s.lower()
    # counter to get frequency distribution
    freq_dist = Counter(s)
    # ordered dict to get first unique character
    unique_chars = OrderedDict(freq_dist)
    first_unique_char_index = None
    # iterate over ordered dict to find index of first unique char
    for char in unique_chars:
        if unique_chars[char] == 1:
            first_unique_char_index = s.index(char)
            break
    # sort frequency distribution
    sorted_freq_dist = sorted(freq_dist.items())
    return {
        'first_unique_char_index': first_unique_char_index,
        'frequency_dist': sorted_freq_dist
    }