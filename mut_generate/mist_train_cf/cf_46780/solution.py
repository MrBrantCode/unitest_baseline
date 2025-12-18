"""
QUESTION:
Create a function `is_nested_and_balanced(s)` that takes a string `s` as input and returns a boolean indicating whether the string has balanced parentheses, square brackets, curly braces, and angle brackets, with proper nesting and interleaving of matching symbols. The function should use a stack data structure to store the opening symbols and check for matching closing symbols. The function should return `True` if the string is balanced and `False` otherwise.
"""

def is_nested_and_balanced(s):
    stack = []
    openers_to_closers = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    closers = set(openers_to_closers.values())

    for char in s: 
        if char in openers_to_closers:
            stack.append(char)
        elif char in closers:
            if not stack: 
                return False
            else: 
                last_unclosed_opener = stack.pop()
                if not char == openers_to_closers[last_unclosed_opener]:
                    return False

    return stack == [] 