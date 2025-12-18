"""
QUESTION:
Design a function `encode(message)` that accepts a string of up to 100 characters containing spaces, punctuation, and alphabetic characters. The function should return a string containing only the alphabetic characters from the input message, effectively removing spaces and punctuation.
"""

def encode(message):
    """
    This function encodes a given message by removing spaces and punctuation.
    
    Args:
        message (str): A string containing up to 100 characters.
    
    Returns:
        str: A string containing only the alphabetic characters from the input message.
    """
    return ''.join(filter(str.isalpha, message))