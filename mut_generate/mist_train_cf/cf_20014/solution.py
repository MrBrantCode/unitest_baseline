"""
QUESTION:
Create a function called `add_two_numbers(a, b)` that takes two numbers as input. The function should return the sum of the two numbers if both are positive and their sum is not divisible by 3. If either of the input numbers is negative, the function should return "Error: Negative numbers not allowed". If the sum of the two numbers is divisible by 3, the function should return "Error: Sum is divisible by 3".
"""

def add_two_numbers(a, b):
    """
    This function adds two numbers and returns the sum if both are positive and their sum is not divisible by 3.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int or str: The sum of a and b if both are positive and their sum is not divisible by 3, 
                    "Error: Negative numbers not allowed" if either a or b is negative, 
                    "Error: Sum is divisible by 3" if the sum of a and b is divisible by 3.
    """
    if a < 0 or b < 0:
        return "Error: Negative numbers not allowed"
    if (a + b) % 3 == 0:
        return "Error: Sum is divisible by 3"
    return a + b