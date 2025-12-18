"""
QUESTION:
Create a function `correct_bracketing` that takes a string `brackets` consisting only of parentheses characters ('(' and ')') and returns `True` if all parentheses match and are nested appropriately, `False` otherwise.
"""

def correct_bracketing(brackets):
    stack = []
    for ch in brackets:
        if ch == '(':
            # An opening bracket is always accepted.
            stack.append(ch)
        elif ch == ')':
            # A closing bracket is only accepted if it can match an opening one.
            if not stack or stack.pop() != '(':
                return False
    # If there's any unmatched opening bracket at the end, it's an error.
    return not stack