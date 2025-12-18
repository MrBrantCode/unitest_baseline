"""
QUESTION:
Create a function named `identify_datatype` that takes one input parameter and returns a string representing its datatype. The function should support the following datatypes: integers, floats, strings, booleans, lists, tuples, dictionaries, and sets. If the datatype is not one of these, return "Unknown Datatype".
"""

def identify_datatype(input_parameter):
    if isinstance(input_parameter, int):
        return "Integer"
    elif isinstance(input_parameter, float):
        return "Float"
    elif isinstance(input_parameter, str):
        return "String"
    elif isinstance(input_parameter, bool):
        return "Boolean"
    elif isinstance(input_parameter, list):
        return "List"
    elif isinstance(input_parameter, tuple):
        return "Tuple"
    elif isinstance(input_parameter, dict):
        return "Dictionary"
    elif isinstance(input_parameter, set):
        return "Set"
    else:
        return "Unknown Datatype"