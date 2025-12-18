"""
QUESTION:
Create a function named `convert_list_to_string` that takes a list of integers as input and returns a string of comma-separated values. The function should not include any spaces between the commas and values. The input list will only contain integers.
"""

def convert_list_to_string(lst):
    """
    This function takes a list of integers as input and returns a string of comma-separated values.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    str: A string of comma-separated values.
    """
    return ','.join(map(str, lst))