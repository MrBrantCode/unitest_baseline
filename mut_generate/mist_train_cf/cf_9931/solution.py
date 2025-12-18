"""
QUESTION:
Reverse the words of a given English sentence and convert all vowels to uppercase. The function should take a string as input and return the modified string. The function name should be `reverse_and_convert`.
"""

def reverse_and_convert(s):
    """
    This function takes a string as input, reverses the order of words, 
    and converts all vowels to uppercase.

    Args:
    s (str): The input string.

    Returns:
    str: The modified string.
    """
    vowels = 'aeiouAEIOU'
    words = s.split()
    words = [word if not any(char in vowels for char in word) 
             else ''.join(char.upper() if char.lower() in 'aeiou' else char for char in word) 
             for word in words]
    return ' '.join(reversed(words))