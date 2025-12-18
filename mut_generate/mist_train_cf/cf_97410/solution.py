"""
QUESTION:
Create a function called `replace_hello` that takes a string as an argument. The function should replace the word "Hello, " with "Goodbye, " in the input string, but only if "Hello, " appears at the beginning of the string, is case-sensitive, and only replaces the first occurrence. The function should return the modified string.
"""

def replace_hello(sentence):
    """
    Replaces the word "Hello, " with "Goodbye, " at the beginning of a string.
    
    Args:
        sentence (str): The input string.
    
    Returns:
        str: The modified string with "Hello, " replaced by "Goodbye, ".
    """
    return sentence.replace("Hello, ", "Goodbye, ", 1)