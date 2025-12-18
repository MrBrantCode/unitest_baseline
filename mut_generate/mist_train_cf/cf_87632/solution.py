"""
QUESTION:
Create a function `calculate_frequency` that takes a string as input and returns a list of tuples, where each tuple contains a character and its frequency. The function should ignore case sensitivity, remove punctuation marks and special characters, and sort the characters by frequency in descending order. The input string can have a maximum length of 10^5 characters, and the function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output.
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