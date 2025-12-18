"""
QUESTION:
Create a function called `process_string` that takes a string `s` as input. The function should remove consecutive repeating characters from the string, order the unique characters in descending order based on their frequency, and sort characters with the same frequency alphabetically. The function should return a tuple containing the resulting string and a dictionary where the keys are the unique characters and the values are their frequencies.
"""

from collections import Counter

def process_string(s):
    # Count character occurrence
    char_freq = Counter(s)

    # Sort by frequency descending, then character ascending
    sorted_chars = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))

    # Create the resulting string
    result = ''.join([char * freq for char, freq in sorted_chars])

    # Create the frequency dictionary
    freq_dict = {char: freq for char, freq in sorted_chars}

    return result, freq_dict