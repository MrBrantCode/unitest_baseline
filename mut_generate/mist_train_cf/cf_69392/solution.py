"""
QUESTION:
Write a function named `match_parens_brackets` that takes a list of two strings consisting only of open and closed parentheses and brackets. The function should return 'Yes' if the two strings can be combined in any order to form a properly nested parentheses and brackets string, and 'No' otherwise.
"""

def match_parens_brackets(lst):
    s = ''.join(lst)

    stack = []
    mapping = {')': '(', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return 'No'
        else:
            return 'No'

    if stack:
        return 'No'
    else:
        return 'Yes'