"""
QUESTION:
Create a function called `primitive_or_non_primitive_data_types` that takes a data type as input and returns whether it is a primitive or non-primitive data type. Consider the following data types: byte, short, int, long, float, double, char, boolean, String, Arrays, Classes, and Enums. The function should return 'primitive' if the input data type is primitive, 'non-primitive' if it is non-primitive, and 'invalid' if the input data type is not recognized.
"""

def primitive_or_non_primitive_data_types(data_type):
    """
    This function determines whether a given data type is primitive or non-primitive.

    Args:
    data_type (str): The input data type.

    Returns:
    str: 'primitive' if the input data type is primitive, 'non-primitive' if it is non-primitive, and 'invalid' if the input data type is not recognized.
    """
    primitive_types = ['byte', 'short', 'int', 'long', 'float', 'double', 'char', 'boolean']
    non_primitive_types = ['String', 'Arrays', 'Classes', 'Enums']

    if data_type in primitive_types:
        return 'primitive'
    elif data_type in non_primitive_types:
        return 'non-primitive'
    else:
        return 'invalid'