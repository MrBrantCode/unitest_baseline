"""
QUESTION:
Write a function `separate_words_and_numbers(input_string)` that takes a string of words, numbers, and special characters as input and returns two lists: one containing the words as strings and the other containing the numbers as floats. The function should ignore special characters, remove any leading or trailing special characters from each word, and separate the words and numbers correctly. The input string can contain multiple special characters.
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