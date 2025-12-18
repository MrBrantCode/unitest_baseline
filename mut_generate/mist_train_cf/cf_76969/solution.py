"""
QUESTION:
Write a function named `replace_exclamation` that takes a string as input and returns the string with every occurrence of an exclamation mark (!) replaced with an underscore (_). The input string is "ExCLaMAtiONs ArE Loud!".
"""

def replace_exclamation(s):
    """
    Replaces every occurrence of an exclamation mark (!) with an underscore (_).
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The string with every exclamation mark replaced with an underscore.
    """
    return s.replace('!', '_')