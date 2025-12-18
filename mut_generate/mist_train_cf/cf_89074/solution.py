"""
QUESTION:
Create a function `separate_words_and_numbers` that takes an input string containing words, numbers, and special characters. Separate the words and numbers into two lists, where words are strings and numbers are floats. Remove any leading and trailing special characters from each word and ignore all special characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re

def separate_words_and_numbers(input_string):
    # Extract words and numbers using regular expressions
    words = re.findall(r'\b[a-zA-Z]+\b', input_string)
    numbers = [float(num) for num in re.findall(r'\d+\.\d+', input_string)]

    return words, numbers