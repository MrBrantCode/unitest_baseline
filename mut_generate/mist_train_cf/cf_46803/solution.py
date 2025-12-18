"""
QUESTION:
Write a function `match_parens(lst)` that takes a list of two strings consisting only of parentheses '(', ')' and squared brackets '[', ']'. The function should check if the concatenation of the strings results in a correctly nested parentheses and brackets string and return 'Yes' if valid, 'No' otherwise.
"""

def match_parens(lst):
    s = ''.join(lst) 
    stack = []
    mapping = {')':'(', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return 'No'
    return 'Yes' if not stack else 'No'