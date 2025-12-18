"""
QUESTION:
Given a list of integers, write a function named `third_highest_number` to find the third highest number in the list. The function should take a list of integers as input and return an integer. If there are less than three unique numbers in the list, the function should handle the case accordingly.
"""

def third_highest_number(numbers):
    """
    This function finds the third highest number in a given list of integers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The third highest number in the list. If there are less than three unique numbers, 
         it returns None or handles the case accordingly.
    """
    # Remove duplicates and sort the list in descending order
    unique_numbers = sorted(set(numbers), reverse=True)
    
    # Check if there are at least three unique numbers
    if len(unique_numbers) < 3:
        return None  # or handle the case accordingly
    
    # Return the third highest number
    return unique_numbers[2]