"""
QUESTION:
Write a function called `sum_of_even_numbers` that calculates the sum of all even numbers in a given list using only a while loop. The function should take a list of integers as input and return the sum of the even numbers.
"""

def sum_of_even_numbers(numbers):
    """
    This function calculates the sum of all even numbers in a given list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The sum of the even numbers in the list.
    """
    index = 0
    sum_of_even = 0
    
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            sum_of_even += numbers[index]
        index += 1
    
    return sum_of_even