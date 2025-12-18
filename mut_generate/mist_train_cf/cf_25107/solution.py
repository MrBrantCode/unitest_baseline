"""
QUESTION:
Create a function `and_gate_3` that implements a three-input AND gate. The function should take three boolean inputs and return `True` only if all inputs are `True`, otherwise return `False`.
"""

def and_gate_3(a, b, c):
    """
    This function implements a three-input AND gate.
    
    Parameters:
    a (bool): The first input.
    b (bool): The second input.
    c (bool): The third input.
    
    Returns:
    bool: True if all inputs are True, False otherwise.
    """
    return a and b and c