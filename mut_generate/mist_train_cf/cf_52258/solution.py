"""
QUESTION:
Create a function `find_min_frequency_number` that takes a sequence of float values as input and returns the number with the minimum frequency of appearances in the sequence. If multiple numbers have the same minimum frequency, the function should return the first one it encounters.
"""

from collections import Counter

def find_min_frequency_number(sequence):
    # Calculating frequencies of each number
    freq_dict = Counter(sequence)

    # Initialize minimum frequency to infinity and number to None
    min_freq = float('inf')
    num = None

    # Iterating through the frequency dictionary to find the number with min frequency
    for k, v in freq_dict.items():
        if v < min_freq:
            min_freq = v
            num = k

    return num