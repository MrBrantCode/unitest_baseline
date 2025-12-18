"""
QUESTION:
Develop a function named `match_quote` that takes a string `text` as input and returns a boolean value. The function should use a regular expression to match the quote "You can't judge a book by its cover" in the input string, ignoring changes in capitalization and punctuation. The function should consider the word order and exact wording of the quote, and it should not match if the words are in a different order or if any word is missing.
"""

import re

def match_quote(text):
    # Removing all punctuations but apostrophes
    text = re.sub(r"[^\w\s']",' ', text)
    text = re.sub(r'\s+', ' ', text)   # removing extra spaces if there are any
    
    # The regular expression pattern 
    pattern = re.compile(r'you can\'t judge a book by its cover', re.IGNORECASE)
    
    # perform search
    match = pattern.search(text)
    
    # If match found, return True else False
    return match is not None