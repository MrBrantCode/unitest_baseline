"""
QUESTION:
Given a list of strings consisting only of open and close parentheses, determine if it's possible to concatenate these strings in a certain order to form a properly nested string of parentheses. Write a function `match_parens(lst)` that returns 'Yes' if such an order exists and 'No' otherwise.
"""

def match_parens(lst):
    total = ''.join(lst)
    stack = []

    for char in total:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: 
               return 'No'
            stack.pop()  

    return 'Yes' if not stack else 'No'