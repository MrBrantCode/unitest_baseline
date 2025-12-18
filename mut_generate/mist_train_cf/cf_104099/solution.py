"""
QUESTION:
Write a function called `determine_datatype` that takes a numeric input and returns its datatype. The input will be a numeric value with or without a decimal point. Determine the datatype based on the presence of a decimal point.
"""

def determine_datatype(num):
    """
    This function determines the datatype of a given numeric input.
    
    Parameters:
    num (numeric): A numeric value with or without a decimal point.
    
    Returns:
    str: The datatype of the input number.
    """
    if isinstance(num, int):
        return "int"
    elif isinstance(num, float):
        return "float"
    else:
        return "unknown"