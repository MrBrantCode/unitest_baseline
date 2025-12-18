"""
QUESTION:
Create a function `divide_numbers(x, y)` that takes two arguments, `x` and `y`, and returns their division result if both are numeric values and not equal. If `x` and `y` are equal, return "Error: x and y are equal". If either `x` or `y` is not a numeric value, return "Error: x and y must be numeric values". If `y` is zero, return "Error: Cannot divide by zero".
"""

def divide_numbers(x, y):
    """
    This function divides two numbers and returns the result.
    
    Args:
        x (int/float): The dividend.
        y (int/float): The divisor.
    
    Returns:
        float: The division result if both are numeric values and not equal.
        str: An error message if x and y are equal, not numeric values, or if y is zero.
    """
    
    # Check if x and y are numeric values
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Error: x and y must be numeric values"
    
    # Check if x and y are equal
    if x == y:
        return "Error: x and y are equal"
    
    # Check if y is zero
    if y == 0:
        return "Error: Cannot divide by zero"
    
    # Perform division
    return x / y