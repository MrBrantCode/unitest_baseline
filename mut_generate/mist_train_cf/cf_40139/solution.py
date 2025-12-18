"""
QUESTION:
Implement the function `validate_expression(expression: str) -> bool` where `expression` is a string of length between 1 and 100 (inclusive), representing a mathematical expression containing integers, arithmetic operators (+, -, *, /), and parentheses. The function should return True if the expression is valid and False otherwise, considering the following rules:
- The expression contains only valid characters.
- The parentheses are balanced.
- The expression follows the rules of arithmetic operations.
"""

def validate_expression(expression: str) -> bool:
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    if stack:
        return False  

    try:
        eval(expression)  
    except SyntaxError:
        return False  

    return True