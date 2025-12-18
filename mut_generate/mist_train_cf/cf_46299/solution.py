"""
QUESTION:
Create a function `check_expression(expr)` that takes a string of mathematical expression as input. The function should return two boolean values. The first indicates whether the expression has balanced parentheses, brackets, and braces. The second indicates whether the expression is syntactically correct, meaning it does not contain any invalid characters or sequences, such as two operators in a row, an operator at the end of the expression, or a number immediately followed by an open parenthesis.
"""

def check_expression(expr):
    # Define valid characters and sequences
    valid_chars = set('0123456789+-*/()[]{} ')
    valid_sequences = {'++', '--', '**', '//', '*/', '/*', '()[]{}'}

    # Check for invalid characters and sequences
    for char in expr:
        if char not in valid_chars:
            return False, False 
    for seq in valid_sequences:
        if seq in expr:
            return False, False 

    # Check for operator at the end of the expression
    if expr[-1] in '+-*/':
        return False, False

    # Check for number immediately followed by open parenthesis
    for i in range(len(expr) - 1):
        if expr[i].isdigit() and expr[i + 1] in '([{':
            return False, False 

    # Check for balanced parentheses, brackets, and braces
    stack = []
    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False, False
            if char == ')' and stack.pop() != '(':
                return False, False
            if char == ']' and stack.pop() != '[':
                return False, False 
            if char == '}' and stack.pop() != '{':
                return False, False 
    if stack:
        return False, False 

    return True, True 