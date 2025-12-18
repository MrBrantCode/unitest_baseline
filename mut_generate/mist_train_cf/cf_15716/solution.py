"""
QUESTION:
Write a function `select_items` that takes a list of strings, a list of integers representing indexes, a string of alphabet keys, and a boolean flag indicating whether duplicates are allowed. The function should return a list of items from the list at the specified indexes, corresponding to the alphabet keys, or None if the maximum index value exceeds the length of the alphabet string. If duplicates are allowed, return all items; otherwise, return unique items.
"""

def select_items(list_of_strings, indexes, alphabet_string, allow_duplicates):
    """
    Select items from a list of strings based on given indexes and alphabet keys.

    Args:
    list_of_strings (list): A list of strings.
    indexes (list): A list of integers representing indexes.
    alphabet_string (str): A string of alphabet keys.
    allow_duplicates (bool): A boolean flag indicating whether duplicates are allowed.

    Returns:
    list: A list of items from the list at the specified indexes, or None if the maximum index value exceeds the length of the alphabet string.
    """
    if max(indexes) >= len(alphabet_string):
        return None
    
    selected_items = [list_of_strings[index] for index in indexes if index < len(list_of_strings)]
    
    if not allow_duplicates:
        selected_items = list(set(selected_items))
    
    return selected_items