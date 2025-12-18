"""
QUESTION:
Write a function `custom_histogram(test)` that takes a string of space-separated letters and returns a dictionary where each key is a letter in lowercase followed by its count (e.g., 'a_1', 'b_2') and the value is the count of that letter. The function should ignore special characters, be case-insensitive, and include all letters with the same frequency in the output.
"""

import re

def custom_histogram(test):
    # Remove all special characters and split into words
    test = re.sub('[^A-Za-z ]+', '', test)

    # Transform to lowercase
    test = test.lower()

    # Split the string into letters
    letters = test.split(' ')

    # Create a dictionary
    histogram = {}

    # For each letter, increase the count in the dictionary
    for letter in set(letters):
        if letter:
            histogram[letter + '_' + str(letters.count(letter))] = letters.count(letter)

    return histogram