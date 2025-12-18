"""
QUESTION:
Write a function named `detect_data_type` that takes one argument. The function should return the data type of the given argument as a string. It should return "integer" if the argument is an integer, "float" if it is a float, and "string" if it is a string. If the argument is a list, the function should return the data type of its first element. If the argument is a dictionary, the function should return the data type of the value of its first key. If the argument is of any other data type or if it is an empty list or dictionary, the function should return "unknown".
"""

def detect_data_type(var):
    if isinstance(var, int):
        return "integer"
    elif isinstance(var, float):
        return "float"
    elif isinstance(var, str):
        return "string"
    elif isinstance(var, list):
        if len(var) == 0:
            return "unknown"  # Empty list
        else:
            return detect_data_type(var[0])
    elif isinstance(var, dict):
        if len(var) == 0:
            return "unknown"  # Empty dictionary
        else:
            return detect_data_type(list(var.values())[0])
    else:
        return "unknown"