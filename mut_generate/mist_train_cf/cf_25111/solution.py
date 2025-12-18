"""
QUESTION:
Write a function named `find_largest_even` that takes a list of integers as input and returns the largest even number in the list. If no even numbers are found in the list, the function should return "No even numbers in the list."
"""

def find_largest_even(lst):
    """
    This function finds the largest even number in a list of integers.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The largest even number in the list. If no even numbers are found, returns "No even numbers in the list."
    """
    even_nums = [num for num in lst if num % 2 == 0]
    return max(even_nums) if even_nums else "No even numbers in the list."