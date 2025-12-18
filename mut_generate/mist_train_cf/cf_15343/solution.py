"""
QUESTION:
Create a function `remove_chars(strings, characters)` that takes a list of strings and a set of characters as inputs. The function should return a new list where all characters in the set have been removed from each string, and any resulting empty strings have been removed. The function should handle empty input lists and sets containing non-alphanumeric characters.
"""

def remove_chars(strings, characters):
    if not strings:
        return []

    result = []
    for string in strings:
        string = ''.join(char for char in string if char not in characters)
        if string:
            result.append(string)
    
    return result