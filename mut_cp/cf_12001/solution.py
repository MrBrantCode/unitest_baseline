"""
ORIGINAL QUESTION:
Create a function `calculate` that evaluates a string representing a mathematical expression. The expression can include parentheses and exponentiation. The function should return the result of the evaluated expression. The expression is valid and well-formed, and it only contains digits, operators (+, -, *, /, ^), and parentheses. The input string does not contain any whitespace characters.
"""

import math

def calculate(expression):
    expression = expression.replace(' ', '')  # Remove any whitespace
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            stack.append('(')
            i += 1
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            i += 1
        elif expression[i] in operators:
            while stack and stack[-1] in operators and priority[expression[i]] <= priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(expression[i])
            i += 1
        else:
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            output.append(float(num))
    
    while stack:
        output.append(stack.pop())
    
    stack = []
    for token in output:
        if isinstance(token, float):
            stack.append(token)
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(math.pow(a, b))
    
    return stack[0]