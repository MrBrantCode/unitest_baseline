"""
QUESTION:
Write a Python function named `transition_indefinite_to_definite` that takes a string as input, replaces all occurrences of " a " with " the ", and returns the resulting string. The replacement should be case-sensitive and consider " a " as a whole word to avoid replacing "a" within other words.
"""

def transition_indefinite_to_definite(input_string):
    """
    Replaces all occurrences of " a " with " the " in a given string.
    
    Args:
        input_string (str): The input string to perform the replacement on.
    
    Returns:
        str: The resulting string after replacing " a " with " the ".
    """
    return input_string.replace(" a ", " the ")