"""
QUESTION:
Separate the words and numbers from a given input string into two separate lists. The input string can contain multiple special characters. The words should be separated into a list of strings, while the numbers should be separated into a list of floats. Any special characters should be ignored, and all leading and trailing special characters should be removed from each word in the word list.

The function name should be `separate_words_and_numbers`, and it should take one argument: `input_string`. The function should return two lists: one for the words and one for the numbers.
"""

import re

def separate_words_and_numbers(input_string):
    # Remove leading and trailing special characters
    input_string = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', input_string)
    
    # Separate words and numbers using regular expressions
    words = re.findall(r'[a-zA-Z]+', input_string)
    numbers = re.findall(r'[0-9.]+', input_string)
    
    # Convert numbers to floats
    numbers = [float(num) for num in numbers]
    
    return words, numbers