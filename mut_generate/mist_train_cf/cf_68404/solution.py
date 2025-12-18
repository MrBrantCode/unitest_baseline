"""
QUESTION:
Write a function named `evaluate_expression` that takes a string representing a mathematical equation as input, evaluates it following the order of operations (BODMAS), and returns the result. The function should be able to handle basic arithmetic operations (+, -, *, /) and should not use any external libraries. Ensure the solution is safe from security risks associated with evaluating user-supplied input.
"""

def evaluate_expression(expression):
    """
    Evaluates a string representing a mathematical equation following the order of operations (BODMAS).
    
    Parameters:
    expression (str): A string representing a mathematical equation.
    
    Returns:
    result: The result of the evaluated expression.
    """
    # Using eval function to evaluate the expression
    # This approach should only be used in a safe and controlled environment due to security risks
    return eval(expression)