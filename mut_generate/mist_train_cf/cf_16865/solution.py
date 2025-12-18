"""
QUESTION:
Create a function named `create_dict` that takes a list of tuples as input where each tuple contains a character and a number. Using dictionary comprehension, map the characters to their corresponding numbers and return the resulting dictionary.
"""

def create_dict(tuples_list):
    """
    This function takes a list of tuples as input where each tuple contains a character and a number.
    It maps the characters to their corresponding numbers using dictionary comprehension and returns the resulting dictionary.

    Args:
        tuples_list (list): A list of tuples, each containing a character and a number.

    Returns:
        dict: A dictionary mapping characters to their corresponding numbers.
    """
    return {key: value for key, value in tuples_list}