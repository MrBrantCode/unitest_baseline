"""
QUESTION:
Create a function `reverse_polish_notation_evaluator(expression, substitution_dict)` that evaluates an expression written in reverse Polish notation. The function should take two parameters: `expression`, a string of space-separated tokens representing the reverse Polish notation, and `substitution_dict`, a dictionary where keys are variable names and values are either integers or variable names. If a variable name is used as a value in the dictionary, it should be replaced with its corresponding value. The function should return the evaluated result of the expression.
"""

from operator import add, sub, mul

def reverse_polish_notation_evaluator(expression, substitution_dict):
    opers = {
        '+': add,
        '-': sub,
        '*': mul
    }
    stack = []

    substitution_dict = { key: substitution_dict[substitution_dict[key]] if substitution_dict[key] in substitution_dict else substitution_dict[key] for key in substitution_dict}

    for item in expression.split():
        if item in opers:
            val2 = stack.pop()
            val1 = stack.pop()
            operation = opers[item]
            stack.append(operation(val1, val2))
        elif item in substitution_dict:
            stack.append(int(substitution_dict[item]))
        else:
            stack.append(int(item))

    return stack[0]