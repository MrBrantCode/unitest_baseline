"""
QUESTION:
Create a function called `encode_parentheses` that takes a string of parentheses as input and returns a dictionary. The function should convert each set of parentheses into a string where an open parenthesis is represented as 'x' and a close parenthesis is represented as 'y'. The dictionary should have the length of each set of parentheses as the key and the corresponding encoded string as the value. The function should ignore any spaces in the input string.
"""

from typing import Dict

def entrance(paren_string: str) -> Dict[int, str]:
    result = {}
    item = ''
    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            item += 'x'
        if char == ')':
            item += 'y'
            if len(item) in result:
                result[len(item)] += item
            else:
                result[len(item)] = item
            item = ''
    return result