"""
QUESTION:
Replace all occurrences of "A" with "#" and "W" with "$" in a given string, then reverse the order of the characters. The function should take a string as input and return the modified string.
"""

def entrance(sentence):
    """
    Replaces 'A' with '#' and 'W' with '$' in the input string, 
    then reverses the order of characters.

    Args:
        sentence (str): The input string.

    Returns:
        str: The modified string.
    """
    return sentence.replace("A", "#").replace("W", "$")[::-1]