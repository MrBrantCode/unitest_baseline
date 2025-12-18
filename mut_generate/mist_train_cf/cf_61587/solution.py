"""
QUESTION:
Write a function `infixToPostfix(infix_expression)` that converts an infix expression to a postfix expression. The function should take a string `infix_expression` as input, where operands are single characters from A to Z and operators are ^, *, /, +, -. The input expression does not contain spaces and follows the standard infix notation rules. The function should return the equivalent postfix expression as a string.
"""

def infixToPostfix(infix_expression):
    # Define the precedence of operators
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # Initialize empty stack and postfix string
    stack = [] 
    postfix = ''

    for char in infix_expression:
        # If operand, add it to output
        if char.isalpha():
            postfix += char
        # If '(', push it to stack
        elif char == '(':
            stack.append('(')
        # If ')', pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        # If operator, pop until less precendence operator is found
        else:
            while stack and stack[-1]!='(' and precedence[char]<=precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)

    # Pop remaining elements in stack
    while stack:
        postfix += stack.pop()

    return postfix