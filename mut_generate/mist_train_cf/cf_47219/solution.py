"""
QUESTION:
Create a function `separate_data_types` that takes a string of space-separated values as input. The function should identify each value as an integer, float, or string, store them in separate lists, and return these lists. If a value cannot be converted to an integer or float, it should be treated as a string. The function should handle invalid input and assume the input might be an integer first, then a float, and finally a string if the previous conversions fail.
"""

def separate_data_types(input_string):
    """
    Separate the input string of space-separated values into integers, floats, and strings.
    
    Parameters:
    input_string (str): A string of space-separated values.
    
    Returns:
    tuple: Three lists containing integers, floats, and strings respectively.
    """
    
    int_list = []
    float_list = []
    str_list = []
    
    # Split the input string into a list
    user_list = input_string.split()
    
    # For each item in the list, try to cast to each type
    for item in user_list:
        try:
            # Try to cast the item to int. If successful, add to int_list
            int_list.append(int(item))
        except ValueError:
            try:
                # If it can't be cast to int, try to cast to float. 
                # If successful, add to float_list
                float_list.append(float(item))
            except ValueError:
                # If it can't be cast to either numerical type, treat it as a string.
                # Add to str_list
                str_list.append(item)
                
    return int_list, float_list, str_list