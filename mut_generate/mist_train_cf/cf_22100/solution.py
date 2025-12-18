"""
QUESTION:
Create a function named unique_elements that takes a list of integers as input and returns a list containing unique integers in the order of their first occurrence. The function should not use any built-in functions or libraries.
"""

def unique_elements(input_list):
    """
    This function takes a list of integers as input and returns a list containing unique integers in the order of their first occurrence.

    :param input_list: A list of integers
    :return: A list of unique integers in the order of their first occurrence
    """
    unique_list = []
    
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list