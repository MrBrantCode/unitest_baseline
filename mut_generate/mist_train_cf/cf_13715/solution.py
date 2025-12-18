"""
QUESTION:
Create a function named `create_dictionary` that takes a list of tuples as input. Each tuple contains a key and a value, and possibly a data type. The function should return a dictionary where the key is the first element of the tuple and the value is the second element of the tuple, transformed according to the following rules:

- If the key is a string, the value is converted to uppercase.
- If the key is an integer, the value is converted to its binary representation.
- If the key is a float, the value is rounded to the nearest whole number.
- If the tuple contains a third element, it specifies the data type of the value, and the value is converted to that type (int, float, or bin).
"""

def create_dictionary(list_of_tuples):
    """
    Create a dictionary from a list of tuples, transforming values based on key type or specified data type.

    Args:
    list_of_tuples (list): A list of tuples, each containing a key, a value, and optionally a data type.

    Returns:
    dict: A dictionary where keys are the first element of each tuple and values are transformed according to the specified rules.
    """
    dictionary = {}
    for tup in list_of_tuples:
        key, value = tup[0], tup[1]
        if len(tup) == 3:
            data_type = tup[2]
            if data_type == int:
                value = int(value)
            elif data_type == float:
                value = round(value)
            elif data_type == bin:
                value = bin(value)
        else:
            if isinstance(key, str):
                value = value.upper()
            elif isinstance(key, int):
                value = bin(value)
            elif isinstance(key, float):
                value = round(value)
        dictionary[key] = value
    return dictionary