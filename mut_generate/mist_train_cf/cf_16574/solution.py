"""
QUESTION:
Implement a function named `evaluate_expression` that takes a string expression as input, evaluates it according to the order of operations, and returns the final result. The expression may contain multiple nested parentheses, complex mathematical operations, and exponential calculations (e.g., 2^3). The function should handle the expression from left to right, following the standard order of operations (PEMDAS/BODMAS).
"""

def evaluate_expression(expression):
    """
    Evaluates a mathematical expression according to the order of operations.
    
    Args:
    expression (str): A string containing the mathematical expression to be evaluated.
    
    Returns:
    float: The result of the evaluated expression.
    """
    # Replace ^ with ** for exponential calculations
    expression = expression.replace('^', '**')
    
    # Evaluate the expression using eval function
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)