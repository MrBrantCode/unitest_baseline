"""
QUESTION:
Write a function named `gathered_characters` to extract unique characters from a given string, considering case sensitivity, and return them in sorted order. The function should be implemented using list comprehension or set.
"""

def gathered_characters(input_string):
    """
    Extract unique characters from a given string, considering case sensitivity, 
    and return them in sorted order.
    
    Args:
        input_string (str): The input string to extract unique characters from.
    
    Returns:
        list: A list of unique characters in the input string, in sorted order.
    """
    return sorted(list(set(input_string)))