"""
QUESTION:
Create a function `first_last_chars` that takes a list of strings as input and returns a new list of strings. Each element in the new list should be a string made up of the first and last character of the corresponding element in the original list. If the element in the original list is empty, ignore it and do not include it in the new list. If the element in the original list is a single character, duplicate it to create the new string. The input list will only contain strings.
"""

def first_last_chars(strings):
    """
    Given a list of strings, returns a new list where each element is a string made up of the first and last character of the corresponding element in the original list.
    
    If the element in the original list is empty, it is ignored and not included in the new list.
    If the element in the original list is a single character, it is duplicated to create the new string.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        list: A new list of strings.
    """
    return [word[0] + word[-1] if len(word) > 1 else word * 2 for word in strings if word]