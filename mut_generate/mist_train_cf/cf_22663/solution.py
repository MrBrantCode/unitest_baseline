"""
QUESTION:
Create a function called `reverse_unique_words` that takes a string as input and returns an array of unique words from the string in reverse order. The function should ignore any punctuation marks and consider uppercase and lowercase letters as the same word. The function should not take any other parameters.
"""

import string

def reverse_unique_words(s):
    # Convert string to lowercase
    s = s.lower()
    
    # Remove punctuation marks
    translator = str.maketrans("", "", string.punctuation)
    s = s.translate(translator)
    
    # Split string into words
    words = s.split()
    
    # Create a set to store unique words
    unique_words = set(words)
    
    # Convert set to list and reverse it
    return list(unique_words)[::-1]