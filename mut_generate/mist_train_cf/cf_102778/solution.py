"""
QUESTION:
Write a function called `sum_odd_numbers` that calculates the sum of all odd numbers between a lower limit and an upper limit (inclusive), where both limits are positive integers greater than 1. The function should take two parameters, `lower_limit` and `upper_limit`, and return the sum of the odd numbers between them.
"""

def sum_odd_numbers(lower_limit, upper_limit):
    """
    This function calculates the sum of all odd numbers between a lower limit and an upper limit (inclusive).
    
    Parameters:
    lower_limit (int): The lower limit (inclusive) of the range of numbers.
    upper_limit (int): The upper limit (inclusive) of the range of numbers.
    
    Returns:
    int: The sum of all odd numbers between the lower and upper limits.
    """
    sum_odd_numbers = 0
    for num in range(lower_limit, upper_limit + 1):
        if num % 2 != 0:  # check if the number is odd
            sum_odd_numbers += num
    return sum_odd_numbers