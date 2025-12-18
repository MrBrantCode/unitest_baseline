"""
QUESTION:
Create a function `filter_vowel_odd_length` that takes a list of strings as input and returns a new list containing only the strings that start with a vowel and have an odd length. The list should be created using list comprehension.
"""

def filter_vowel_odd_length(strings):
    """
    Returns a new list containing only the strings that start with a vowel and have an odd length.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        list: A new list containing filtered strings.
    """
    return [string for string in strings if string[0].lower() in "aeiou" and len(string) % 2 != 0]