"""
QUESTION:
Create a function `modifyTenthElement` that takes an associative array with at least 1000 elements as input. The function should set the key of the tenth element to "bar" and modify its value to "Hello World". The function should return the modified array. The input array should be modified in-place.
"""

def modify_tenth_element(array):
    """
    Modify the tenth element of an associative array.
    
    Parameters:
    array (dict): The input dictionary with at least 1000 elements.
    
    Returns:
    dict: The modified dictionary with the key of the tenth element set to "bar" and its value set to "Hello World".
    """
    # Convert the dictionary items to a list to access the tenth element
    items = list(array.items())
    
    # Get the key of the tenth element
    tenth_key = items[9][0]
    
    # Update the key of the tenth element to "bar"
    array["bar"] = array.pop(tenth_key)
    
    # Update the value of the tenth element to "Hello World"
    array["bar"] = "Hello World"
    
    return array