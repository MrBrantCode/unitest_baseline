"""
QUESTION:
Implement a function `classify_word(word)` that classifies a given word as a noun, verb, or adjective based on the following rules: 
- Capital letter and ends with "ing": verb
- Lowercase letter and ends with "ing": adjective
- Capital letter and ends with "ed": noun
- Lowercase letter and ends with "ed": verb
- Capital letter and more than two syllables: noun
- Lowercase letter and more than two syllables: verb
- Lowercase letter and ends with "y": adjective.
"""

def classify_word(word):
    """
    Classify a word as a noun, verb, or adjective based on given rules.

    Parameters:
    word (str): The word to be classified.

    Returns:
    str: The classification of the word (noun, verb, adjective, or unknown).
    """
    # Check if the word starts with a capital letter
    if word[0].isupper():
        # Check if the word ends with "ing"
        if word.endswith("ing"):
            return "verb"
        # Check if the word ends with "ed" or has more than two syllables
        elif word.endswith("ed") or len(word.split()) > 2:
            return "noun"
    else:
        # Check if the word ends with "ing"
        if word.endswith("ing"):
            return "adjective"
        # Check if the word ends with "ed"
        elif word.endswith("ed"):
            return "verb"
        # Check if the word ends with "y"
        elif word.endswith("y"):
            return "adjective"

    return "unknown"