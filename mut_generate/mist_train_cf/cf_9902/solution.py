"""
QUESTION:
Design a function `getSum` that adds two integers without using the '+' operator. The integers can be positive or negative. The function should return the sum of the two integers. The solution must only use bitwise operations.
"""

def getSum(num1: int, num2: int) -> int:
    """
    This function adds two integers without using the '+' operator.
    
    Parameters:
    num1 (int): The first integer to be added.
    num2 (int): The second integer to be added.
    
    Returns:
    int: The sum of num1 and num2.
    """
    
    # Continue the loop until num2 becomes 0
    while num2 != 0:
        # Calculate the sum of num1 and num2 using bitwise XOR operation
        sum = num1 ^ num2
        
        # Calculate the carry using bitwise AND operation and left shift
        num2 = (num1 & num2) << 1
        
        # Update num1 for the next iteration
        num1 = sum
    
    # Return the sum
    return num1