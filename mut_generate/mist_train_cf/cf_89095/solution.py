"""
QUESTION:
Write a function named `check_balanced(expression)` to check if the parentheses, curly brackets, square brackets, and angle brackets in a given expression are balanced or not. If the brackets are balanced and the angle brackets are properly nested, the function should return `True`. If the brackets are not balanced or the angle brackets are not properly nested, the function should return `False` if there are unbalanced brackets, otherwise it should return the position of the first occurrence of the incorrectly nested angle brackets.
"""

def check_balanced(expression):
    stack = []
    angle_brackets_stack = []
    angle_brackets_positions = []
    
    for i, char in enumerate(expression):
        if char in '([{<':
            stack.append(char)
            if char == '<':
                angle_brackets_stack.append('<')
                angle_brackets_positions.append(i)
        elif char in ')]}>':
            if not stack:
                return False
            top = stack.pop()
            if char == ')':
                if top != '(':
                    return False
            elif char == ']':
                if top != '[':
                    return False
            elif char == '}':
                if top != '{':
                    return False
            elif char == '>':
                if top != '<':
                    return False
                angle_brackets_stack.pop()
                angle_brackets_positions.pop()
    
    if stack or angle_brackets_stack:
        return False
    
    if angle_brackets_positions:
        return angle_brackets_positions[0]
    
    return True