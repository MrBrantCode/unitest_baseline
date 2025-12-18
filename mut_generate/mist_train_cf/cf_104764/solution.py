"""
QUESTION:
Implement the `handle_input_value` function to categorize input integers into ranges and return the corresponding result. The function should handle values less than 0 as "negative", 0 as "zero", and positive integers within specific ranges (single digit, double digit, triple digit, etc.) using separate conversion functions (`convert_single_digit`, `convert_double_digit`, `convert_triple_digit`, etc.), and out of range values as "out of range".
"""

def convert_single_digit(i):
    return f"single digit number: {i}"

def convert_double_digit(i):
    return f"double digit number: {i}"

def convert_triple_digit(i):
    return f"triple digit number: {i}"

def handle_input_value(i):
    """
    This function categorizes input integers into ranges and returns the corresponding result.
    
    Args:
        i (int): The input integer value.
    
    Returns:
        str: The category of the input integer value.
    """
    if i < 0:
        return "negative"
    elif i == 0:
        return "zero"
    elif i < 10:
        return convert_single_digit(i)
    elif i < 100:
        return convert_double_digit(i)
    elif i < 1000:
        return convert_triple_digit(i)
    else:
        return "out of range"