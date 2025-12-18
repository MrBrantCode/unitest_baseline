"""
QUESTION:
Create a function named `convert_to_postfix(expression)` that converts a given infix mathematical expression to postfix notation. The function should handle alphabetic characters (representing variables) and the four basic arithmetic operators (+, -, *, /) along with parentheses to maintain the correct order of operations. The function should return the resulting postfix expression as a string.
"""

def convert_to_postfix(expression):
    stack = []
    postfix = []
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    
    for char in expression:
        if char.isalpha():
            postfix.append(char)
        elif char in operators:
            if char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and operators[char] <= operators[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)