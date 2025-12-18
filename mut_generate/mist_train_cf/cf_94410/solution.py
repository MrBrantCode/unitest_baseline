"""
QUESTION:
Create a function `convert_to_postfix(expression)` that takes a string `expression` representing an infix mathematical expression and returns its equivalent postfix notation as a string. The function should handle parentheses and the basic arithmetic operators (+, -, *, /). The `expression` string only contains uppercase English letters and the basic arithmetic operators.
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