"""
QUESTION:
Create a function `convert_list_to_dict` that takes a list as input and returns a dictionary where the keys are the unique items from the list and the values are their corresponding first occurrence positions in the list. The function should exclude any duplicate items in the list.
"""

def convert_list_to_dict(input_list):
    """
    This function takes a list as input and returns a dictionary where the keys are the unique items 
    from the list and the values are their corresponding first occurrence positions in the list.
    
    Args:
        input_list (list): The input list to be converted to a dictionary.
    
    Returns:
        dict: A dictionary with unique items from the list as keys and their first occurrence positions as values.
    """
    output_dict = {}
    for index, item in enumerate(input_list):
        if item not in output_dict:
            output_dict[item] = index
    return output_dict