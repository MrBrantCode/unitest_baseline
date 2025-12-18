"""
QUESTION:
Create a function named `extract_pattern` that takes two parameters: `text` and `pattern`. The function should return the number of occurrences of the `pattern` in the `text` and a new string resulting from removing all occurrences of the `pattern` from the `text`. The function should be case-sensitive and consider spaces and punctuation as part of the pattern.
"""

def extract_pattern(text, pattern):
    """
    This function takes in a text and a pattern, and returns the number of occurrences 
    of the pattern in the text and a new string with the pattern removed.

    Parameters:
    text (str): The original text.
    pattern (str): The pattern to be extracted.

    Returns:
    tuple: A tuple containing the number of occurrences and the new string.
    """
    # Extract occurrences of the pattern
    occurrences = text.count(pattern)
    # Create the resulting new string
    new_string = text.replace(pattern, '')
    return occurrences, new_string