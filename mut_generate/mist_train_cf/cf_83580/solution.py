"""
QUESTION:
Create a function named `correct_bracketing` that takes a string `brackets` containing only "<" and ">" characters. The function should return `True` if every opening bracket "<" has a corresponding closing bracket ">", and `False` otherwise.
"""

def correct_bracketing(brackets):
    stack = []
    
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if len(stack) == 0 or stack[-1] != "<":
                return False
            stack.pop()

    return len(stack) == 0