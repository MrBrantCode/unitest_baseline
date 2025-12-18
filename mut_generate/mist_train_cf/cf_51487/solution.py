"""
QUESTION:
Write a function `match_order_parens(lst)` that takes a list of strings containing only '(' or ')' as input. The function should return 'Yes' if a valid nested parentheses string can be formed by concatenating the strings in a specific order, and 'No' otherwise. A valid nested parentheses string has correctly ordered and nested parentheses pairs, such as '(()())'. The function should validate the nesting and order of the parentheses pairs.
"""

def match_order_parens(lst):
    string = ''.join(lst)
    parentheses_stack = []

    for i in string:
        if i == '(':
            parentheses_stack.append(i)
        else:
            if not parentheses_stack:
                return 'No'
            parentheses_stack.pop()

    if parentheses_stack:
        return 'No'

    return 'Yes'