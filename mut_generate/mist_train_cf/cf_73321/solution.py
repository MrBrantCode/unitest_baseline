"""
QUESTION:
Create a function named `check_balance` that takes a mathematical expression as input and returns a boolean indicating whether the expression has balanced parentheses, where every opening bracket has a corresponding closing bracket in the correct order. The function should handle three types of parentheses: round brackets `()`, curly brackets `{}`, and square brackets `[]`.
"""

def check_balance(expression):
    stack = []
    
    for char in expression:
        if char in ["(", "{", "["]: 
            stack.append(char)
        elif char in [")", "}", "]"]: 
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
              return False
            elif char == "}" and stack[-1] != "{":
              return False
            elif char == "]" and stack[-1] != "[":
              return False
            stack.pop()

    return not stack