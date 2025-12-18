"""
QUESTION:
Write a function `evaluate_expression(x, y)` that takes two integers `x` and `y` as input and returns `True` if the expression `((x + y) % 3 == 0 and (x * y) % 6 == 0 and abs(x - y) <= 6)` evaluates to `True`, and `False` otherwise.
"""

def evaluate_expression(x, y):
    """
    Evaluate the expression ((x + y) % 3 == 0 and (x * y) % 6 == 0 and abs(x - y) <= 6).
    
    Args:
        x (int): The first integer.
        y (int): The second integer.
    
    Returns:
        bool: True if the expression evaluates to True, False otherwise.
    """
    return (x + y) % 3 == 0 and (x * y) % 6 == 0 and abs(x - y) <= 6