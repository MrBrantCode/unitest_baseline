"""
QUESTION:
Write a function named `separate_words_and_numbers` that takes an input string as a parameter and returns two lists. The first list should contain the words from the input string as strings, with any leading or trailing special characters removed. The second list should contain the numbers from the input string as floats. Special characters should be ignored. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re

def separate_words_and_numbers(input_string):
    words = re.findall(r'\b[a-zA-Z]+\b', input_string)
    numbers = [float(num) for num in re.findall(r'\d+\.\d+', input_string)]
    return words, numbers