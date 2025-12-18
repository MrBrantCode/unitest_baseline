"""
QUESTION:
Create a function named `string_formatter` that takes a string `input_string` as input and returns a list of unique words in alphabetical order. The function should ignore any punctuation marks and consider words with different capitalizations as the same word. The time complexity of the solution should be O(n log n) or better. The function should remove any duplicate words and return a sorted list of unique words.
"""

import re

def string_formatter(input_string):
    # Convert input string to lowercase and remove punctuation marks
    input_string = re.sub(r'[^\w\s]', '', input_string.lower())
    
    # Split the input string into a list of words
    words = input_string.split()
    
    # Remove duplicates and sort the list of words
    unique_words = sorted(set(words))
    
    return unique_words