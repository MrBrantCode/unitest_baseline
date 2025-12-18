"""
QUESTION:
Create a function called `solve_expression` that evaluates a user-entered mathematical expression and prints the result, following the order of operations (BIDMAS). The expression may contain integers, addition (+), subtraction (-), multiplication (*), and division (/). The function should handle invalid expressions, such as division by zero or unbalanced brackets, and print an error message in such cases.
"""

def solve_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return "The entered expression is invalid."