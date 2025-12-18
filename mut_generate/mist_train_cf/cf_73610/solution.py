"""
QUESTION:
Create a function named `error_parens` that takes a list of two strings consisting only of '(' or ')' as input. The function should return 'Valid' if combining the strings creates a correctly nested and balanced sequence of parentheses, and 'Invalid' otherwise. The function must ensure that there are never more ')' than '(' parentheses at any point in the sequence.
"""

def error_parens(lst):
    combined = ''.join(lst)
    balance = 0
    for char in combined:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return 'Invalid'
    return 'Valid' if balance == 0 else 'Invalid'