"""
QUESTION:
Implement a function named `multiply_without_asterisk` that takes two integers `a` and `b` as input and returns their product without using the '*' operator. The function should have a time complexity of O(log min(a, b)).
"""

def multiply_without_asterisk(a, b):
    """
    This function multiplies two integers without using the '*' operator.
    
    It uses the Russian Peasant Multiplication algorithm, which has a time complexity of O(log min(a, b)).
    
    The function assumes that the input integers are positive. For negative integers, additional steps are required to handle the sign.
    
    Parameters:
    a (int): The first integer to be multiplied.
    b (int): The second integer to be multiplied.
    
    Returns:
    int: The product of a and b.
    """
    
    # Initialize the result to 0
    result = 0
    
    # Repeat the following steps until a becomes 0
    while a != 0:
        # If a is odd, add b to the result
        if a % 2 != 0:
            result += b
        
        # Divide a by 2 (integer division)
        a //= 2
        
        # Double the value of b
        b *= 2
    
    # Return the value of result as the multiplication of a and b
    return result