"""
QUESTION:
Create a function called `transmute_dictionary` that takes a dictionary as input and returns a new dictionary where each key-value pair is swapped. The original dictionary should not be modified. The function should work for any dictionary where the values can be used as keys (i.e., they are immutable and unique).
"""

def transmute_dictionary(input_dict):
    """
    This function takes a dictionary as input and returns a new dictionary 
    where each key-value pair is swapped. The original dictionary is not modified.
    
    Args:
        input_dict (dict): The dictionary to be transmuted.
    
    Returns:
        dict: A new dictionary where each key-value pair is swapped.
    """
    return {value: key for key, value in input_dict.items()}