"""
QUESTION:
Complete the solution so that it returns the number of times the search_text is found within the full_text. 

Usage example:
"""

def count_occurrences(full_text: str, search_text: str) -> int:
    """
    Counts the number of times `search_text` appears in `full_text`.

    Parameters:
    - full_text (str): The main text in which to search.
    - search_text (str): The substring to count within `full_text`.

    Returns:
    - int: The number of occurrences of `search_text` in `full_text`.
    """
    return full_text.count(search_text)