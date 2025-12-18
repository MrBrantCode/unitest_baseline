"""
QUESTION:
Create a function `sorted_dict_from_list` that takes a list as input and returns a dictionary. The keys in the dictionary should be the elements from the list that are of type string, all keys should be unique, and all values should be of the same data type. The dictionary should be sorted in descending order based on the length of the keys.
"""

from collections import OrderedDict

def sorted_dict_from_list(lst):
    """
    This function takes a list as input, creates a dictionary with string elements from the list as keys, 
    ensures unique keys, same data type for values, and returns a dictionary sorted in descending order based on key length.

    Args:
        lst (list): A list containing elements of different data types.

    Returns:
        OrderedDict: An ordered dictionary with string elements as keys and values of the same data type.
    """

    # Filter out non-string elements and store them in a separate list to determine the data type for values
    non_string_elements = [element for element in lst if not isinstance(element, str)]
    
    # If there are no non-string elements, use None as the value data type
    if not non_string_elements:
        value_type = type(None)
    else:
        # Determine the data type of the first non-string element
        value_type = type(non_string_elements[0])
    
    # Filter out string elements and store them in a separate list
    string_elements = [element for element in lst if isinstance(element, str)]
    
    # Create a dictionary with string elements as keys and values of the same data type
    dict_from_list = {key: value_type() for key in string_elements}
    
    # Sort the dictionary in descending order based on key length
    sorted_dict = OrderedDict(sorted(dict_from_list.items(), key=lambda item: len(item[0]), reverse=True))
    
    return sorted_dict