"""
QUESTION:
Write a function `find_frantic_sentences(text)` that takes a string `text` as input and returns a list of sentences containing the word 'frantic'. The function should use regular expressions to match sentences and handle edge cases such as abbreviations and acronyms.
"""

import re
def find_frantic_sentences(text):
    # Define the pattern to match sentences containing the word 'frantic'
    pattern = r'([A-Z][^.!?]*frantic[^.!?]*[.!?])'
    
    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)
    
    # Return the list of matched sentences
    return matches