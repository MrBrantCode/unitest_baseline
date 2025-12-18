"""
QUESTION:
Implement a function `calculate_result` that takes three parameters `a`, `b`, and `c`, and returns a result based on the value of `a`. If `a` is 0, return `b` multiplied by `c`. If `a` is 1, return `b` added to `c`. For any other value of `a`, return `b` subtracted by `c`.
"""

def calculate_result(a, b, c):
    """
    Returns a result based on the value of 'a'.
    
    If 'a' is 0, returns 'b' multiplied by 'c'.
    If 'a' is 1, returns 'b' added to 'c'.
    For any other value of 'a', returns 'b' subtracted by 'c'.
    
    Parameters:
    a (int): The decision variable.
    b (int): The first operand.
    c (int): The second operand.
    
    Returns:
    int: The calculated result.
    """
    if a == 0:
        return b * c
    elif a == 1:
        return b + c
    else:
        return b - c