"""
QUESTION:
Create a function called `evaluate` that takes a string expression as input, parses it, and evaluates the mathematical expression with the given variables. The expression should support basic arithmetic operations (+, -, *, /), single variables, and handle errors like division by zero. Additionally, create a function called `substitute_vars` that takes the expression and a dictionary of variable values, replaces the variables in the expression with their corresponding values, and returns the updated expression.
"""

def evaluate(expression, vars):
    def divide(x, y):
        if y == 0:
            return 'Error! Division by zero.'
        else:
            return x / y

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': divide
    }

    # finding every operation on same level of parentheses
    for char in '-+/':
        if char in expression:
            left, op, right = expression.partition(char)
            return operations[char](evaluate(left, vars), evaluate(right, vars))

    if '*' in expression:
        left, op, right = expression.partition('*')
        return operations[op](evaluate(left, vars), evaluate(right, vars))

    # base case
    expression = expression.replace(' ', '') # remove extra spaces
    if expression.isdigit():
        return int(expression)
    else: # assuming single variables
        return vars.get(expression, 0)

def substitute_vars(expr, var_values):
    for k in var_values.keys():
        expr = expr.replace(k, str(var_values[k]))
    return expr