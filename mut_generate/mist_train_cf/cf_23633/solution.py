"""
QUESTION:
Write a function called `second_highest` that finds the second highest value in a given array of integers. The input array will contain at least two distinct elements.
"""

def second_highest(numbers):
    """
    This function finds the second highest value in a given array of integers.
    
    Parameters:
    numbers (list): A list of integers containing at least two distinct elements.
    
    Returns:
    int: The second highest value in the list.
    """
    numbers = list(set(numbers))  # Remove duplicates
    numbers.sort(reverse=True)  # Sort in descending order
    return numbers[1]  # Return the second highest value