"""
QUESTION:
Create a function `capitalize_first_letter` that takes a list of strings as input and returns a new list of strings with the first letter of each non-empty string capitalized. The function should achieve a time complexity of O(n), where n is the total number of characters in all strings combined. The function should not use any built-in string manipulation functions such as `capitalize()` or `title()`.
"""

def capitalize_first_letter(names):
    return [name[0].upper() + name[1:] if name != "" else name for name in names]