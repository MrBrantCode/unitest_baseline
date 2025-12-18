"""
QUESTION:
Write a function named `validate_nested_parens_brackets` that takes a list of two strings as input. The strings only contain opening and closing parentheses and brackets. The function should return `True` if the strings can be combined sequentially to form a perfectly nested string, and `False` otherwise. The rules for a perfectly nested string are: every opening parenthesis or bracket must have a corresponding closing one, and an opening parenthesis or bracket may have other opening parentheses or brackets inside it, which must be closed within the outer one.
"""

def validate_nested_parens_brackets(lst):
    stack = []
    lookup = {")": "(", "]": "["}
    
    concatenated_string = ''.join(lst)    
    for char in concatenated_string:
        if char in lookup.values():    
            stack.append(char)    
        elif char in lookup.keys():
            if stack == [] or lookup[char] != stack.pop():
                return False    
    return stack == []    