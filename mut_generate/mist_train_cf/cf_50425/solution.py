"""
QUESTION:
Write a function called `find_frequency` that takes a string as input and returns two dictionaries: one for the frequency of each distinct letter in the string (ignoring case sensitivity) and another for the frequency of all pairs of adjacent letters.
"""

from collections import defaultdict

def find_frequency(string):
    single_letter_freq = defaultdict(int)
    pair_letter_freq = defaultdict(int)
    
    norm_string = string.lower()

    # single letter frequency
    for letter in norm_string:
        single_letter_freq[letter] += 1
    
    # pair letter frequency
    for i in range(len(norm_string) - 1):
        pair = norm_string[i:i+2]
        pair_letter_freq[pair] += 1

    return single_letter_freq, pair_letter_freq