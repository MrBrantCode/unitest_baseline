"""
QUESTION:
Create a function named `convert_to_dict` that takes a list of tuples as input where each tuple contains a full name and a unique identifier. The function should return a dictionary where the unique identifiers are the keys and the full names are the values. Use only Python-built functions and avoid in-built looping constructs to ensure efficiency and readability.
"""

def convert_to_dict(tuples_list):
    """
    This function takes a list of tuples as input where each tuple contains a full name and a unique identifier.
    It returns a dictionary where the unique identifiers are the keys and the full names are the values.

    Args:
        tuples_list (list): A list of tuples containing full names and unique identifiers.

    Returns:
        dict: A dictionary with unique identifiers as keys and full names as values.
    """
    # Reversing the 'key' and 'value' order in the tuple list, using the map function
    reversed_tuples = map(lambda x: (x[1], x[0]), tuples_list)
    
    # Converting the tuple list to dictionary
    result_dict = dict(reversed_tuples)
    
    return result_dict