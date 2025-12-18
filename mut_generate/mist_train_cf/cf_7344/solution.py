"""
QUESTION:
Create a function called `arithmetic_operations` that takes two integers `a` and `b` as parameters and performs addition, subtraction, multiplication, and division operations. The function should return a dictionary containing the results of these operations. The division result should be rounded to the nearest integer. If division by zero occurs, the function should handle this error and return an error message instead of the division result.
"""

def arithmetic_operations(a, b):
    """
    This function performs addition, subtraction, multiplication, and division operations.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    dict: A dictionary containing the results of the operations.
    """
    
    result = {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b
    }
    
    if b != 0:
        result['division'] = round(a / b)
    else:
        result['division'] = "Error: Cannot divide by zero"
    
    return result