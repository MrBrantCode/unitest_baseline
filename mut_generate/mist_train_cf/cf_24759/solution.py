"""
QUESTION:
Create a function `transform_list_to_dict` that takes a list of unique strings as input and returns a dictionary where the keys are the elements of the list and the values are set to True.
"""

def transform_list_to_dict(input_list):
    """
    This function transforms a list of unique strings into a dictionary 
    where the keys are the elements of the list and the values are set to True.
    
    Args:
        input_list (list): A list of unique strings.
    
    Returns:
        dict: A dictionary where the keys are the elements of the list and the values are set to True.
    """
    return {element: True for element in input_list}