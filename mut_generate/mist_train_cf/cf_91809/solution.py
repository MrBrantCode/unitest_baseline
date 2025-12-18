"""
QUESTION:
Write a Python function `match_sentence` that takes a string as input and returns `True` if the string matches the pattern "an apple a day keeps the doctor away" with the following variations: 
- Different capitalization of letters 
- Extra spaces between words 
- Substituting "apple" with synonyms 
- Substituting "doctor" with synonyms 
- Adding or removing punctuation marks 
- Pluralizing or singularizing words.
"""

import re

def match_sentence(sentence):
    """
    Returns True if the input sentence matches the pattern 
    "an apple a day keeps the doctor away" with variations.
    
    Parameters:
    sentence (str): The input sentence to be matched.
    
    Returns:
    bool: True if the sentence matches the pattern, False otherwise.
    """
    
    pattern = r"(?i)\b(an|a) (apple|fruit) (a|one) (day|daily) keeps? (the|a) (doctor|physician|healthcare provider)(s?) away\b"
    return bool(re.search(pattern, sentence))