"""
QUESTION:
Create a function named `process_tuples` that takes a list of tuples as input. The function should create a dictionary where the key is the first element of each tuple and the value is the second element of the tuple. The value should be converted based on the first element's data type or the specified data type in a tuple with three elements. The conversion rules are as follows: 
- if the first element is a string or the specified data type is string, the value should be converted to uppercase;
- if the first element is an integer or the specified data type is integer, the value should be converted to its binary representation;
- if the first element is a float or the specified data type is float, the value should be rounded to the nearest whole number. 
The function should have a time complexity of O(n), where n is the number of tuples in the list, and a space complexity of O(1), not using any additional data structures or variables that scale with the input size.
"""

def process_tuples(tuples):
    """
    Process a list of tuples into a dictionary where the key is the first element of each tuple
    and the value is the second element of the tuple, converted based on the first element's data type
    or the specified data type in a tuple with three elements.

    Args:
        tuples (list): A list of tuples.

    Returns:
        dict: A dictionary of processed key-value pairs.
    """
    dictionary = {}
    for tpl in tuples:
        if len(tpl) == 3:
            key = tpl[0]
            value = tpl[1]
            data_type = tpl[2]
            if data_type == str:
                value = str(value).upper()
            elif data_type == int:
                value = bin(value)[2:]
            elif data_type == float:
                value = round(value)
        else:
            key = tpl[0]
            value = tpl[1]
            if isinstance(key, str):
                value = str(value).upper()
            elif isinstance(key, int):
                value = bin(value)[2:]
            elif isinstance(key, float):
                value = round(value)
        dictionary[key] = value
    return dictionary