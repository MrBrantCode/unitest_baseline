"""
QUESTION:
Create a function called `math_bracket_sorter(expr)` that takes a string `expr` containing a mathematical expression with parentheses '()', square brackets '[]', and curly braces '{}' as input. The function should return 'Correct' if the expression has a balanced and valid arrangement of brackets, and 'Incorrect' otherwise.
"""

def math_bracket_sorter(expr):
    open_br = ['(', '[', '{']
    close_br = [')', ']', '}']
    match_br = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in expr:
        if char in open_br:
            stack.append(char)
        elif char in close_br:
            if not stack or match_br[stack.pop()] != char:
                return 'Incorrect'

    return 'Correct' if not stack else 'Incorrect'