"""
QUESTION:
Write a function named `lambda_handler` that takes an integer `n` as input and returns the sum of the first `n` Lucas numbers. The Lucas sequence is similar to the Fibonacci sequence, but with initial values 2 and 1. The function should have a time complexity of O(n) and should not use any built-in functions or libraries to calculate the Lucas sequence.
"""

def lambda_handler(n):
    """
    Calculate the sum of the first n Lucas numbers.

    Args:
    n (int): The number of Lucas numbers to sum.

    Returns:
    int: The sum of the first n Lucas numbers.
    """
    
    # Calculate the sum of the first n Lucas numbers
    sum_lucas = 0
    lucas_1 = 2
    lucas_2 = 1
    
    if n == 1:
        sum_lucas = lucas_1
    elif n > 1:
        sum_lucas = lucas_1 + lucas_2
        
        for i in range(2, n):
            lucas_i = lucas_1 + lucas_2
            sum_lucas += lucas_i
            
            lucas_1 = lucas_2
            lucas_2 = lucas_i
    
    return sum_lucas