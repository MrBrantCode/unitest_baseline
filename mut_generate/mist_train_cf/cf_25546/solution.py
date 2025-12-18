"""
QUESTION:
Create a function named `int_to_word` that takes an integer `i` as input, where `0 ≤ i ≤ 2`, and returns a string representation of the number ("zero", "one", or "two").
"""

def int_to_word(i):
    """
    Returns a string representation of the integer i, where 0 ≤ i ≤ 2.
    
    Args:
        i (int): The input integer.

    Returns:
        str: The string representation of the number ("zero", "one", or "two").
    """
    return ["zero", "one", "two"][i]