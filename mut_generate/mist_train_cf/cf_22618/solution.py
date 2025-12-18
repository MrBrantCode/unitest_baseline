"""
QUESTION:
Write a function `infix_to_postfix` that takes a string representing an infix expression as input and returns the equivalent postfix expression. The infix expression may contain positive and negative integers, variables, operators (+, -, *, /, %, ^), function calls using lowercase alphabets followed by parentheses, and parentheses to indicate the order of operations.
"""

def infix_to_postfix(infix_expr):
    precedence = {
        '+': 1, '-': 1,
        '*': 2, '/': 2, '%': 2,
        '^': 3
    }

    stack = []
    postfix_expr = ''

    i = 0
    while i < len(infix_expr):
        if infix_expr[i].isalnum():
            j = i
            while i < len(infix_expr) and infix_expr[i].isalnum():
                i += 1
            postfix_expr += infix_expr[j:i] + ' '
        elif infix_expr[i] == '(':
            stack.append(infix_expr[i])
            i += 1
        elif infix_expr[i] == ')':
            while stack[-1] != '(':
                postfix_expr += stack.pop() + ' '
            stack.pop()
            i += 1
        elif infix_expr[i] == ',':
            while stack and stack[-1] != '(':
                postfix_expr += stack.pop() + ' '
            i += 1
        elif infix_expr[i] in precedence:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[infix_expr[i]]:
                postfix_expr += stack.pop() + ' '
            stack.append(infix_expr[i])
            i += 1
        else:
            i += 1

    while stack:
        postfix_expr += stack.pop() + ' '

    return postfix_expr.strip()