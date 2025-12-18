"""
QUESTION:
Create a function called `create_dict_from_lists` that takes two lists, `list1` and `list2`, of the same length as input. The function should return a dictionary where the keys are the elements of `list1` converted to uppercase and suffixed with "KEY", and the values are the elements of `list2` converted to integers and incremented by 10. The dictionary should only contain unique keys and should be sorted in descending order based on the values.
"""

def create_dict_from_lists(list1, list2):
    """
    Creates a dictionary where the keys are the elements of list1 converted to uppercase and suffixed with "KEY",
    and the values are the elements of list2 converted to integers and incremented by 10.
    
    Args:
        list1 (list): List of strings to be used as keys.
        list2 (list): List of strings to be used as values.
    
    Returns:
        dict: A dictionary with unique keys and sorted in descending order based on the values.
    """
    
    # Initialize an empty dictionary
    result_dict = {}
    
    # Iterate over the indices of list1 and list2
    for i in range(len(list1)):
        # Create a key by converting the element of list1 to uppercase and adding the suffix "KEY"
        key = list1[i].upper() + "KEY"
        
        # Create the corresponding value by converting the element of list2 to an integer and adding 10 to it
        value = int(list2[i]) + 10
        
        # Add this key-value pair to the dictionary result_dict
        result_dict[key] = value
    
    # Sort the dictionary result_dict in descending order based on the values of the keys
    result_dict = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[1], reverse=True)}
    
    # Return the resulting dictionary
    return result_dict