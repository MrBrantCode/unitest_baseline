"""
QUESTION:
Create a function named `replace_vowels_with_asterisk` that takes a string as input and returns a new string where all vowels are replaced with asterisks (*). The function should consider both lowercase and uppercase vowels.
"""

def replace_vowels_with_asterisk(message):
    """
    This function takes a string as input and returns a new string where all vowels are replaced with asterisks (*).
    
    Args:
        message (str): The input string.
    
    Returns:
        str: A new string where all vowels are replaced with asterisks.
    """
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        message = message.replace(vowel, '*')
    return message