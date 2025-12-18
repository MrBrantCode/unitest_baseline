"""
QUESTION:
Write a function named `sum_even_elements` that takes a list of integers as input, and returns the sum of the even elements in the list, excluding any element greater than 10. The input list contains only positive integers.
"""

def sum_even_elements(numbers):
    """
    This function takes a list of integers as input, and returns the sum of the even elements in the list, 
    excluding any element greater than 10.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The sum of even elements in the list, excluding any element greater than 10.
    """
    return sum(num for num in numbers if num % 2 == 0 and num <= 10)