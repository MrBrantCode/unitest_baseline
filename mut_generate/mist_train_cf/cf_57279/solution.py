"""
QUESTION:
Create a function named `identify_data_type` that takes one input argument of any datatype and categorizes it into one of the following categories: Integer, Floating Point Number, String, List, Dictionary, Tuple, Boolean, or Other. The function should use the built-in Python `type()` function to determine the datatype and should support all built-in Python datatypes.
"""

def identify_data_type(input_entity):
    """
    This function takes an input entity of any datatype and categorizes it into one of the following categories:
    Integer, Floating Point Number, String, List, Dictionary, Tuple, Boolean, or Other.

    Args:
        input_entity (any): The input entity to be categorized.

    Returns:
        str: The category of the input entity.
    """

    data_type = type(input_entity)

    if data_type is int:
        category = "Integer"
    elif data_type is float:
        category = "Floating Point Number"
    elif data_type is str:
        category = "String"
    elif data_type is list:
        category = "List"
    elif data_type is dict:
        category = "Dictionary"
    elif data_type is tuple:
        category = "Tuple"
    elif data_type is bool:
        category = "Boolean"
    else:
        category = "Other"

    return category