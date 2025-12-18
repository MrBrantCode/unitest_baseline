"""
QUESTION:
Remove all specified characters from a list of strings and filter out empty strings. 

Write a function `remove_chars(strings, characters)` that takes a list of strings `strings` and a set of characters `characters` as inputs. The function should return a new list with all occurrences of characters from `characters` removed from each string in `strings`. If a string becomes empty after removing characters, it should be excluded from the output list. The function should also handle the case where the input list `strings` is empty.
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