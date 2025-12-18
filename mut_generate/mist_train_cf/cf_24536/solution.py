"""
QUESTION:
Write a function named `evaluate` that takes a string mathematical expression as input and returns its result. The function should be able to handle expressions with basic arithmetic operators (+, -, *, /) and should return `None` if the evaluation fails.
"""

def evaluate(expression):
    """
    Evaluate a string mathematical expression and return its result.
    
    Args:
        expression (str): A string mathematical expression.
    
    Returns:
        result: The result of the expression if evaluation is successful, otherwise None.
    """
    result = None
    try:
        result = eval(expression)
    except:
        pass
    return result