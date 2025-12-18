"""
QUESTION:
Write a function called `filter_by_letter_a` that takes a list of strings as input and returns a list of strings containing only the elements from the input list that include the letter 'a'. The function should be case sensitive.
"""

def filter_by_letter_a(s):
    """
    Returns a list of strings containing only the elements from the input list 
    that include the letter 'a'. The function is case sensitive.
    
    Args:
    s (list): A list of strings.
    
    Returns:
    list: A list of strings containing the letter 'a'.
    """
    return [item for item in s if 'a' in item]