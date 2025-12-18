"""
QUESTION:
Develop a function named `find_max_result` that takes a list of integers as input and calculates the result of each number in the list when divided by 5. The result is defined as the sum of the quotient and the remainder of the division. The function should return the maximum result among all numbers in the list.
"""

def find_max_result(numbers):
    """
    Calculate the maximum result among all numbers in the list when divided by 5.
    
    The result is defined as the sum of the quotient and the remainder of the division.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    float: The maximum result among all numbers in the list.
    """
    results = [num / 5 + num % 5 for num in numbers]
    return max(results)