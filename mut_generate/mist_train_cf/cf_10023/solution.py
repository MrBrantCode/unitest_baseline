"""
QUESTION:
Evaluate the given mathematical expression with multiple nested parentheses and complex mathematical operations using the function `evaluate_expression`. The function should take a string of the mathematical expression as input and return the final result. The mathematical expression can contain multiple nested parentheses, addition (+), subtraction (-), multiplication (*), and modulo (%) operators. The function should follow the order of operations (PEMDAS) and handle the operators with the same precedence from left to right.
"""

def evaluate_expression(expression):
    """
    Evaluates the given mathematical expression with multiple nested parentheses and complex mathematical operations.
    
    Args:
    expression (str): The mathematical expression as a string.
    
    Returns:
    int: The final result of the evaluated expression.
    """
    
    # Using the built-in eval function in Python to evaluate the mathematical expression
    return eval(expression)

# Test the function (This is the part that will be excluded)
# print(evaluate_expression("(3 + 5) * 2 - 4 / 2 + 10 % 3 * (6 - 2)"))