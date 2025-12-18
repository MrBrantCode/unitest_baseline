"""
QUESTION:
Create a function named `match_sentence` that uses regular expression to match any given sentence in the English language. The function should consider complexities such as punctuation, capitalization, numbers, special characters, and spacing. The input string is a sentence that may start with an optional leading whitespace, then non-whitespace characters, and concludes at the end of the string or with a period, question mark, or exclamation mark.
"""

import re

def match_sentence(sentence):
    """
    This function uses regular expression to match any given sentence in the English language.
    
    Args:
    sentence (str): A string that may start with an optional leading whitespace, then non-whitespace characters, 
                    and concludes at the end of the string or with a period, question mark, or exclamation mark.
    
    Returns:
    bool: True if the sentence matches the pattern, False otherwise.
    """
    regex_pattern = r'\s*[A-Za-z0-9 ,;:\'\\"-]*[.!?]$'
    match = re.match(regex_pattern, sentence)
    return bool(match)