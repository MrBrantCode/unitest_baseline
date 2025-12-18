"""
QUESTION:
Write a function `concatenate_numbers` that takes a list of integers as input and returns a string where each number from the list is converted to a string and joined together with a hyphen. The function should not take any other arguments besides the list of integers.
"""

def concatenate_numbers(num_list):
    """
    This function takes a list of integers, converts them to strings, 
    and joins them together with a hyphen.

    Args:
        num_list (list): A list of integers.

    Returns:
        str: A string where each number from the list is converted to a string 
             and joined together with a hyphen.
    """
    return '-'.join(map(str, num_list))