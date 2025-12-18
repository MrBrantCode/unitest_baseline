"""
QUESTION:
Correct the given text by replacing incorrect graphical symbols with the correct ones. Implement a function `correct_symbols(text)` that takes a string as input and returns the corrected text. The function should replace multiple spaces with a single space, incorrect dashes (`--`) with hyphens (`-`), three periods (`...`) with an ellipsis (`…`), and incorrect apostrophes (`'`) with right single quotation marks (`’`). The function should not use any external libraries other than the built-in `re` module for regular expressions.
"""

import re

def correct_symbols(text):
    
    # Replace multiple spaces with a single space
    text = re.sub(' +', ' ', text)
    
    # Replace incorrect usage of dash (--) with hyphen (-)
    text = re.sub('--', '-', text)
    
    # Replace incorrect usage of three periods (...) with an ellipsis (…)
    text = re.sub('\.\.\.', '…', text)
    
    # Replace incorrect usage of apostrophe (') with right single quotation mark (’)
    text = re.sub('\'', '’', text)
    
    return text