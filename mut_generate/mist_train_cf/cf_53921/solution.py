"""
QUESTION:
Create a function called `process_input` that takes an integer as input, multiplies it by 2, then adds the original number to the result, and returns the final value. The function should not take any other inputs and should return an output that is three times the originally provided value.
"""

def process_input(n):
    """
    This function takes an integer, multiplies it by 2, then adds the original number to the result, 
    and returns the final value which is three times the originally provided value.

    Args:
        n (int): The input integer.

    Returns:
        int: The final value which is three times the originally provided value.
    """
    return n + (n * 2)