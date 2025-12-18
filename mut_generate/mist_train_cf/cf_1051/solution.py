"""
QUESTION:
Write a Python function named `sum_even_numbers` that calculates the sum of all even numbers in a given list of integers. The function should take a list of integers as input and return the sum of all even numbers in the list.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of all the even numbers in a given list of integers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The sum of all the even numbers in the list.
    """
    sum_even = 0  
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even