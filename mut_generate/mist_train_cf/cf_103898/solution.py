"""
QUESTION:
Create a function named `remove_duplicates_and_uppercase` that takes a string of words as input, converts all the words to uppercase, removes any duplicate words, and returns the result as a string. The order of words in the original string does not matter in the output.
"""

def remove_duplicates_and_uppercase(input_string):
    """
    Converts all words to uppercase, removes any duplicates, and returns the result as a string.
    
    Args:
    input_string (str): A string of words.
    
    Returns:
    str: A string with all words in uppercase and no duplicates.
    """
    words = input_string.upper().split()
    unique_words = set(words)
    return ' '.join(unique_words)