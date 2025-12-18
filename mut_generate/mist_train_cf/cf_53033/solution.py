"""
QUESTION:
Replace all instances of the first person singular pronoun "I" (including those appended with punctuation marks) with the third person singular pronoun "He" in a given string. The function should be named `replace_pronoun` and take a string as input. Note that the solution should handle both standalone "I"s and those immediately followed by punctuation marks, but it may not account for verb form modifications or case variations.
"""

import re

def replace_pronoun(word_string):
    """
    Replace all instances of the first person singular pronoun "I" 
    (including those appended with punctuation marks) with the third person singular pronoun "He" in a given string.

    Args:
    word_string (str): The input string.

    Returns:
    str: The modified string with "I" replaced by "He".
    """
    # Replace standalone 'I' with 'He'
    modified_string = re.sub(r'\bI\b', 'He', word_string)

    # Replace 'I' appended with punctuation marks with 'He'
    modified_string = re.sub(r'\bI(?=[.,;:!?])', 'He', modified_string)

    return modified_string