"""
QUESTION:
Create a function `deduct_if_divisible` that takes an integer `x` as input and returns `x - 10` if `x` is greater than 100 and divisible by 5, otherwise return `x`.
"""

def deduct_if_divisible(x):
    """
    This function deducts 10 from the input integer if it's greater than 100 and divisible by 5.
    
    Parameters:
    x (int): The input integer
    
    Returns:
    int: The result after deduction if the conditions are met, otherwise the original number
    """
    return x - 10 if x > 100 and x % 5 == 0 else x