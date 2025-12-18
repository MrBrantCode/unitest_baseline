"""
QUESTION:
Write a function called `sum_of_largest_two` that takes a list of numbers as input, sorts the list in descending order, and returns the sum of the first two elements. The input list will contain at least two elements.
"""

def sum_of_largest_two(numbers):
    """
    This function takes a list of numbers as input, sorts the list in descending order, 
    and returns the sum of the first two elements.
    
    Args:
        numbers (list): A list of numbers containing at least two elements.
    
    Returns:
        int: The sum of the first two elements of the sorted list.
    """
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]