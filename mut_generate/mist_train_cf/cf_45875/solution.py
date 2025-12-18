"""
QUESTION:
Write a function named `match_parens` that takes a list of two strings composed exclusively of open '(' or closed ')' parentheses. Determine if there exists a sequence of concatenating the strings that results in a properly nested parentheses string. Return 'Yes' if a valid string can be formed, otherwise return 'No'. The input list must contain exactly two strings.
"""

def match_parens(lst):
    '''
    A list of two strings is given, composed exclusively of open '(' or closed ')' parentheses.
    Ascertain if concatenating the strings in a particular sequence results in
    a properly nested parentheses string, e.g., '(())()' is valid, while '())' is not.
    Return 'Yes' if a valid string can be formed, otherwise return 'No'.
    '''
    if len(lst) != 2:
        return 'No'

    s1, s2 = lst
    stack = []
    for ch in s1 + s2:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return 'No'
            stack.pop()

    if not stack:
        return 'Yes'
    return 'No'