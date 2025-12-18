"""
QUESTION:
Write a function named `inverse_dictionary` that takes a dictionary as input and returns an inverted dictionary. The inverted dictionary should contain the original dictionary's values as keys and its keys as values. If there are duplicate values in the original dictionary, they should be stored as a list of corresponding keys in the inverted dictionary.
"""

def inverse_dictionary(dictionary):
    """
    This function takes a dictionary as input and returns an inverted dictionary.
    The inverted dictionary contains the original dictionary's values as keys and its keys as values.
    If there are duplicate values in the original dictionary, they are stored as a list of corresponding keys in the inverted dictionary.

    Args:
        dictionary (dict): The input dictionary to be inverted.

    Returns:
        dict: The inverted dictionary.
    """

    inversed_dictionary = {}
    
    for key, value in dictionary.items():
        if value not in inversed_dictionary:
            inversed_dictionary[value] = [key]
        else:
            inversed_dictionary[value].append(key)
            
    return inversed_dictionary