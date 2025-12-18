"""
QUESTION:
Write a function `find_frantic_sentences` that takes a string as input and returns a list of sentences containing the word 'frantic'. The function should use regular expressions to match sentences and handle edge cases such as abbreviations and acronyms. The function should ignore case sensitivity.
"""

import re

def find_frantic_sentences(text):
    # Define the pattern to match sentences containing the word 'frantic'
    pattern = r'([A-Z][^.!?]*frantic[^.!?]*[.!?])'
 
    # Find all matches of the pattern in the text, ignoring case sensitivity
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
 
    # Return the list of matched sentences
    return matches