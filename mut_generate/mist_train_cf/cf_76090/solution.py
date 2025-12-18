"""
QUESTION:
Write a function called `evaluate_expression` that takes a string representing a mathematical expression as input and returns the result of the expression. The function should be able to handle basic mathematical operations such as addition, subtraction, multiplication, and division, and follow the order of operations. The function should not execute any code that is not a valid mathematical expression.
"""

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression encapsulated in a string format.
    
    Args:
        expression (str): A string representing a mathematical expression.
    
    Returns:
        The result of the mathematical expression.
    
    Note:
        This function uses the eval() built-in function, which can be dangerous if 
        you're evaluating strings that might contain arbitrary code. Use with caution.
    """
    return eval(expression)