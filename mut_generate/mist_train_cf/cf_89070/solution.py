"""
QUESTION:
Create a function `count_unique_characters` that takes a string as input and returns the number of unique characters present in the string. The function should ignore characters surrounded by quotation marks ('"'), single quotation marks ('\''), and parentheses ('(' and ')'). The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def count_unique_characters(s):
    unique_chars = set()
    ignore_chars = ['"', "'", '(', ')']
    to_ignore = False
    ignore_stack = []

    for char in s:
        if char in ignore_chars:
            if char in ['"', "'"] and not to_ignore:
                to_ignore = True
                continue
            elif char in ['"', "'"] and to_ignore:
                to_ignore = False
                continue
            elif char == '(':
                ignore_stack.append(char)
            elif char == ')' and ignore_stack:
                ignore_stack.pop()
        if not to_ignore and char not in ignore_chars:
            unique_chars.add(char)

    return len(unique_chars)