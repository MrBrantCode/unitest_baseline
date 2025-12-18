"""
QUESTION:
Write a function called `detect_data_type` that takes one argument, a variable of any type, and returns a string representing the data type of the variable. If the variable is an integer, float, or string, return "integer", "float", or "string", respectively. If the variable is a list or dictionary, recursively apply the function to the first element or value and return the result. If the variable is of any other type, or if it is an empty list or dictionary, return "unknown". The function should be able to handle variables containing up to 100 elements efficiently.
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