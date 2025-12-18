"""
QUESTION:
Create a function `extract_elements` that takes a 2D list as input and returns a new list where each element is a list containing the first and last element of each sublist in the input list. The input list will contain at least one sublist, and each sublist will contain at least one element.
"""

def extract_elements(my_list):
    """
    This function takes a 2D list as input and returns a new list where each element is a list containing 
    the first and last element of each sublist in the input list.

    Args:
        my_list (list): A 2D list containing at least one sublist, and each sublist contains at least one element.

    Returns:
        list: A new list where each element is a list containing the first and last element of each sublist.
    """
    return [[sub_list[0], sub_list[-1]] for sub_list in my_list]