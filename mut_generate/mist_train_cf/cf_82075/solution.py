"""
QUESTION:
Write a function `error_parens` that takes a list of two strings exclusively composed of '(' or ')' parentheses as input. The function should return 'Valid' if concatenating the strings results in a correctly nested parentheses string and 'Invalid' otherwise.
"""

def error_parens(lst):
    counter = 0
    for s in lst:
        for c in s:
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
            if counter < 0:
                return 'Invalid'
    return 'Valid' if counter == 0 else 'Invalid'