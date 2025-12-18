"""
QUESTION:
Write a function `infix_to_postfix(expr)` that takes an arithmetic expression `expr` in infix notation as input and returns the equivalent expression in postfix notation. The input expression may contain single-letter operands (A-Z), the operators `+`, `-`, `*`, `/`, and parentheses `(` and `)`. The function should follow the standard order of operations and handle parentheses correctly.
"""

def infix_to_postfix(expr):
    stack = []
    postfix = ''

    # Function to check if a character is an operand
    def is_operand(char):
        return char.isalnum()

    # Function to check precedence of operators
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    for char in expr:
        # If the character is an operand, add it to the postfix expression
        if is_operand(char):
            postfix += char
        # If the character is an open parenthesis, push it to the stack
        elif char == '(':
            stack.append(char)
        # If the character is a close parenthesis, pop all operators from the stack and append them to the postfix expression until an open parenthesis is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        # If the character is an operator, pop operators from the stack with higher or equal precedence and append them to the postfix expression, then push the current operator to the stack
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(char)

    # Pop the remaining operators from the stack and append them to the postfix expression
    while stack:
        postfix += stack.pop()

    return postfix