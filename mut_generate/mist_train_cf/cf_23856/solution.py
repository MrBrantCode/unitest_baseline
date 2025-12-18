"""
QUESTION:
Convert the given infix expression to postfix notation using a function named `infix_to_postfix`. The function should take a string representing the infix expression as input and return the corresponding postfix expression as a string. The input string can contain uppercase letters (A-Z) and basic arithmetic operators (+, -, *, /).
"""

def convert_infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = ""
    stack = []
    
    for char in expression:
        if char.isalpha():
            output += char + " "
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop() + " "
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[char]:
                output += stack.pop() + " "
            stack.append(char)
            
    while stack:
        output += stack.pop() + " "
        
    return output.strip()

# No test case