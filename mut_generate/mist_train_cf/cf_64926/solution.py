"""
QUESTION:
Write a function `separate_paren_groups` that takes a string `paren_string` as input, removes any white spaces, and returns a list of strings where each string represents a distinct group of balanced round, square, or curly brackets. Each group does not nest within another group. The function should handle all types of brackets and return the groups in the order they appear in the input string.
"""

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function segregates distinct groups of round, square, and curly brackets into separate string segments.
    Each group is balanced (every opening brace has a corresponding closing brace) and does not nest within another group.
    Disregard any white spaces present in the input string.
    """
    paren_string = paren_string.replace(" ", "")
    start = ['(', '{', '[']
    end = [')', '}', ']']
    groups = []
    temp_string = ''
    counter = 0

    for char in paren_string:
        if char in start:
            counter += 1
            temp_string += char
        elif char in end:
            counter -= 1
            temp_string += char
            if counter == 0:
                groups.append(temp_string)
                temp_string = ''
    return groups