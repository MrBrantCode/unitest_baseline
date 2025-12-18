"""
QUESTION:
Develop a function called `cross_multiply(a, b, c, d)` that takes four numerical entities `a`, `b`, `c`, and `d` as input and performs cross-multiplication using the formula `(a/b) = (c/d)`. The function should return whether the two ratios are equivalent or not. Ensure the function includes error handling measures for zero denominators (`b` or `d`) and non-numerical values.
"""

def cross_multiply(a, b, c, d):
    """
    Perform cross-multiplication and check if two ratios are equivalent.

    Args:
        a (float): The first number of the first ratio.
        b (float): The second number of the first ratio.
        c (float): The first number of the second ratio.
        d (float): The second number of the second ratio.

    Returns:
        str: A message indicating whether the ratios are equivalent or not.
    """

    # Error handling for zero denominators
    if b == 0 or d == 0:
        return "Error: Division by zero is not allowed."
        
    # Error handling for non-numerical values
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or not isinstance(d, (int, float)):
        return "Error: Please enter only numerical values."
        
    # Perform the cross-multiplication and check equivalence
    if a * d == b * c:
        return "The ratios are equivalent."
    else:
        return "The ratios are not equivalent."