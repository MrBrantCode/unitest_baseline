"""
QUESTION:
Create a function called `calculate_result` that takes three parameters `x`, `y`, and `z` and returns the result of a series of mathematical operations. The operations are as follows: 
1. Add `x` and `y` together.
2. Subtract `z` from the result of step 1.
3. Multiply the result of step 2 by `x`.
4. Divide the result of step 3 by `y`.
5. Add the result of step 4 to `y`.
6. Subtract `z` from the result of step 5.
The function should return the final result of these operations.
"""

def calculate_result(x, y, z):
    """
    This function performs a series of mathematical operations and returns the result.
    
    Parameters:
    x (float): The first number
    y (float): The second number
    z (float): The third number
    
    Returns:
    float: The result of the mathematical operations
    """
    # Add x and y together
    result = x + y
    
    # Subtract z from the result of step 1
    result = result - z
    
    # Multiply the result of step 2 by x
    result = result * x
    
    # Divide the result of step 3 by y
    result = result / y
    
    # Add the result of step 4 to y
    result = result + y
    
    # Subtract z from the result of step 5
    result = result - z
    
    return result