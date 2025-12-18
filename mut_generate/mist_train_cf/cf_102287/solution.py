"""
QUESTION:
Write a function `square_and_sort_dict` that takes a dictionary with numeric values as input, squares its values, and returns a new dictionary with the same keys but with the squared values sorted in descending order.
"""

def square_and_sort_dict(input_dict):
    """
    This function squares the values in the input dictionary and returns a new dictionary 
    with the same keys but with the squared values sorted in descending order.
    
    Args:
    input_dict (dict): The input dictionary with numeric values.
    
    Returns:
    dict: A new dictionary with the squared values sorted in descending order.
    """
    
    # Update the dictionary values and square them
    updated_dict = {key: value ** 2 for key, value in input_dict.items()}
    
    # Sort the dictionary based on the squared values in descending order
    sorted_dict = dict(sorted(updated_dict.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_dict