"""
QUESTION:
Write a function named `sum_of_strings` that takes a list of strings as input, where each string represents a positive integer. The function should convert the strings to integers and return their sum. The input list can contain up to 10^6 elements.
"""

def sum_of_strings(lst):
    """
    This function takes a list of strings representing positive integers, 
    converts them to integers, and returns their sum.
    
    Parameters:
    lst (list): A list of strings representing positive integers.
    
    Returns:
    int: The sum of the integers represented by the input strings.
    """
    return sum(int(num) for num in lst)