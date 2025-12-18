"""
QUESTION:
Design a function named `compare_math_expressions` that takes three parameters: two numbers `x` and `y` (which can be integers or real numbers), and a list of mathematical operations `ops` (with a minimum of 2 and a maximum of 10 operations). The function should perform the given operations on the two numbers, compare the results, and return the expression with the highest numerical result. The supported operations are addition, subtraction, multiplication, division, exponentiation, and modulus.
"""

import operator

def compare_math_expressions(x, y, ops):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
        "%": operator.mod
    }
    
    ops = [o for o in ops if o in operations]

    best_result = float('-inf')
    best_expression = None

    for op in ops:
        if op == '/' and y == 0:
            continue  # Avoid division by zero error
        result = operations[op](x, y)
        if result > best_result:
            best_result = result
            best_expression = f"{x} {op} {y}"
    
    return best_expression, best_result