"""
QUESTION:
Write a function `is_symmetrically_enclosed_by` that checks if a given string `str` is symmetrically enclosed by another substring `substr`. The function should return `True` if the string is symmetrically enclosed and `False` otherwise. The function should also consider overlapping occurrences and check if the enclosing substrings are the reverse of each other.
"""

def is_symmetrically_enclosed_by(str, substr):
    str_len = len(str)
    substr_len = len(substr)
    
    if str_len < 2*substr_len:
        return False

    if str[:substr_len] != substr or str[str_len - substr_len:] != substr:
        return False

    return str[:substr_len] == str[str_len - substr_len:][::-1]