"""
QUESTION:
Create a function `count_char_freq` that takes a string `paragraph` as input and returns a dictionary where keys are the characters in the paragraph (excluding none) and values are their frequency counts. The function should be case-insensitive, treating 'I' and 'i' as the same character, and should include digits and special characters. The returned dictionary should have its keys in lower case and sorted in descending order of their frequency counts. If two characters have the same frequency count, they should be in the order of their first occurrence.
"""

import collections

def count_char_freq(paragraph):
    # Convert to lower case
    paragraph = paragraph.lower()

    # Create a dictionary to store the frequency of each character
    char_freq = collections.OrderedDict()

    # Traverse each character in the paragraph
    for char in paragraph:
        if char in char_freq:
            # If the character is already in the dictionary, increment its frequency
            char_freq[char] += 1
        else:
            # If the character is not in the dictionary, add it with frequency 1
            char_freq[char] = 1

    # Sort the dictionary by values in descending order
    char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    return dict(char_freq)