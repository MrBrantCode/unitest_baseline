"""
QUESTION:
Create a function `unique_words(input_string)` that takes a string as input and returns a list of unique words in alphabetical order. The input string should be cleaned by removing punctuation marks and converting all words to lowercase. The input string is limited to a maximum of 200 characters.
"""

import string

def unique_words(input_string):
    # Remove punctuation marks
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    
    # Convert all words to lowercase and split the string into a list of words
    words = input_string.lower().split()
    
    # Create a set to store unique words
    unique_words_set = set(words)
    
    # Sort the unique words alphabetically
    unique_words_list = sorted(list(unique_words_set))
    
    return unique_words_list