"""
QUESTION:
Write a function `extract_hidden_message` that takes a string of words as input and returns a string containing every second letter starting from the second letter using Python string slicing.
"""

def extract_hidden_message(input_string):
    """
    Extracts every second letter from the input string starting from the second letter.
    
    Args:
        input_string (str): The input string from which to extract the hidden message.
    
    Returns:
        str: A string containing every second letter starting from the second letter.
    """
    return input_string[1::2]