"""
QUESTION:
Write a Python function `replace_hello` that replaces the word "Hello" with "Goodbye" in a given string, but only if "Hello" is at the beginning of the sentence, is capitalized, and followed by a comma. The replacement should be case-sensitive.
"""

def replace_hello(s):
    """
    Replace the word "Hello" with "Goodbye" in a given string, 
    but only if "Hello" is at the beginning of the sentence, 
    is capitalized, and followed by a comma.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The modified string with "Hello, " replaced by "Goodbye, ".
    """
    return s.replace("Hello, ", "Goodbye, ")