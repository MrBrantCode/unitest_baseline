"""
QUESTION:
Create a function `evaluate_equation(equation)` that evaluates a mathematical equation given as a string and returns the result. The function should handle potential errors by returning the error message as a string. The equation string is expected to contain only valid mathematical operators and operands.
"""

def evaluate_equation(equation):
    """
    Evaluates a mathematical equation given as a string and returns the result.
    
    Args:
        equation (str): A mathematical equation as a string.
    
    Returns:
        result: The result of the equation if successful, otherwise an error message.
    """
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)