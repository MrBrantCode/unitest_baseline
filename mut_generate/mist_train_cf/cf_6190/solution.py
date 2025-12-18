"""
QUESTION:
Create a function named "sum_of_odd_numbers" that takes an integer n as input and returns the sum of the first n odd numbers. The function should check if the input n is a positive integer and return an error message if it's not. The time complexity of the function should be O(1) and the space complexity should be O(1).
"""

def sum_of_odd_numbers(n):
    """
    This function calculates the sum of the first n odd numbers.
    
    Args:
        n (int): A positive integer indicating the number of odd numbers to sum.
    
    Returns:
        int: The sum of the first n odd numbers if n is a positive integer, otherwise an error message.
    """
    
    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        return "Error: Input should be a positive integer."
    
    # Calculate the sum of the first n odd numbers using the formula: sum = n^2
    sum_of_odds = n ** 2
    
    return sum_of_odds