"""
QUESTION:
Implement a function `evaluate(expression)` that takes a string `expression` containing a mathematical expression and returns the result of the expression. The expression can contain digits, parentheses, and operators '+', '-', '*', '/', and '^'. The function should correctly handle operator precedence and order of operations. Assume that the input expression is valid and does not contain any whitespace characters.
"""

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)
    elif operator == '^':
        values.append(left ** right)

def evaluate(expression):
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while (j < len(expression) and
                    expression[j].isdigit()):
                j += 1
            values.append(int(expression[i:j]))
            i = j-1
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop() 
        else:
            while (operators and
                    operators[-1] != '(' and
                    precedence(expression[i]) <=
                    precedence(operators[-1])):
                apply_operator(operators, values)
            operators.append(expression[i])
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]