"""
QUESTION:
Create a function named `find_largest_numbers` that takes a list of integers as input, returns a list of the largest number(s) excluding any negative numbers.
"""

def find_largest_numbers(numbers):
    """
    This function takes a list of integers as input, 
    returns a list containing the largest number(s) excluding any negative numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    list: A list of the largest number(s) excluding any negative numbers.
    """
    max_num = max([num for num in numbers if num >= 0], default=None)
    if max_num is None:
        return []
    return [num for num in numbers if num == max_num and num >= 0]