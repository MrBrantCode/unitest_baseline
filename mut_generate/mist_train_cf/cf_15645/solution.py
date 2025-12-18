"""
QUESTION:
Calculate the multiplication of two integers without using the '*' operator. The function should have a time complexity of O(log n), where n is the value of the smaller integer, and not use any looping constructs (such as for, while, etc.) or recursion. The function should handle negative integers and return the correct result.
"""

def multiply(a, b):
    """
    Calculate the multiplication of two integers without using the '*' operator.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The product of a and b.
    """
    
    # Define a helper function to perform the multiplication
    def multiply_helper(x, y):
        if y == 0:
            return 0
        # If y is odd, add x to the result
        if y & 1:
            return x + multiply_helper(x << 1, y >> 1)
        # If y is even, multiply x by 2 and divide y by 2
        else:
            return multiply_helper(x << 1, y >> 1)
    
    # Handle negative integers
    if a < 0:
        a, b = b, a
    result = multiply_helper(abs(a), abs(b))
    
    # Negate the result if the original smaller integer was negative
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return result
    else:
        return -result