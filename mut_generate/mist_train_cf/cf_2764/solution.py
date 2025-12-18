"""
QUESTION:
Create a function called `calculate_frequency` that takes an input string, removes punctuation and special characters, ignores case sensitivity, and returns the frequency of each alphabet character in descending order. The function should be able to handle a maximum input string length of 10^5 characters, have a time complexity of O(n), and a space complexity of O(1) excluding the space required for the output.
"""

import collections
import string

def calculate_frequency(input_string):
    # Remove punctuation marks and special characters
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))

    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Count the frequency of each character
    frequency_counter = collections.Counter(input_string)

    # Sort the characters by frequency in descending order
    sorted_characters = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)

    return sorted_characters