"""
QUESTION:
Write a function `is_valid_expression(expr, defined)` that takes a mathematical expression `expr` in string format and a list of defined variables and constants `defined`, and returns `True` if the expression is correctly formatted and `False` otherwise. The function should check for balanced parentheses, valid variable and constant usage, and correct operator-operand sequence, but does not need to validate operator precedence or evaluate the expression. Assume valid variable names are single lowercase letters and valid constants are single uppercase letters.
"""

import re

def is_valid_expression(expr, defined):
    stack = []
    last_char = None
    operators = ['+', '-', '*', '/', '^', 'sqrt']

    for s in re.split('(\W)', expr):
        if s in operators:
            if last_char in operators or last_char is None:
                return False
        elif s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                return False
            stack.pop()
        elif s == ' ':
            continue
        elif s.isalpha():
            if s not in defined:
                return False
        else:  
            if not s.isdigit():
                return False
        last_char = s

    return len(stack) == 0