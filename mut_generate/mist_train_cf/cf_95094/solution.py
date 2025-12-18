"""
QUESTION:
Create a function `remove_empty_strings` that takes a list of strings as input, removes all the empty strings, and returns the new list with non-empty strings in the same order. The function should not use any built-in string or list methods (such as `filter`, `join`, `split`, `index`, `count`, `sort`, `reverse`, `append`, etc.) other than indexing and assignment.
"""

def remove_empty_strings(strings):
    new_list = []
    for element in strings:
        if element != "":
            new_list.append(element)
    return new_list