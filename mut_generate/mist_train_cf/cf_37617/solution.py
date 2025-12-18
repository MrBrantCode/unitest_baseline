"""
QUESTION:
Evaluate the result of a given mathematical expression as a string, considering operator precedence and standard arithmetic rules. The expression contains non-negative integers, four basic arithmetic operators (+, -, *, /), and parentheses. Assume the input expression is always valid and well-formed.

Function Signature: 
def evaluate_math_expression(expression: str) -> int
"""

def evaluate(expression: str) -> int:
    stack = []
    num = 0
    sign = '+'
    for i in range(len(expression)):
        if expression[i].isdigit():
            num = num * 10 + int(expression[i])
        if (not expression[i].isdigit() and expression[i] != ' ') or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = expression[i]
            num = 0
    return sum(stack)