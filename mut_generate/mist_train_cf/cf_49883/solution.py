"""
QUESTION:
Write a function named `find_penultimate_numbers` that takes a list of integers as input and returns the second smallest and second largest numbers in the list. The input list must be sorted in ascending order to determine these values.
"""

def find_penultimate_numbers(numb_list):
    """
    This function takes a list of integers, sorts it in ascending order, 
    and returns the second smallest and second largest numbers.

    Args:
        numb_list (list): A list of integers.

    Returns:
        tuple: A tuple containing the second smallest and second largest numbers.
    """
    numb_list.sort()
    return numb_list[1], numb_list[-2]