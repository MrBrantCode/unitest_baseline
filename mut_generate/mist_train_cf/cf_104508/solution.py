"""
QUESTION:
Convert a list of string digits into a decimal number. The function, `convert_to_decimal`, should take a list of strings as input where each string contains only digits from 0 to 9 and has a maximum length of 3 characters. The function should return a decimal number rounded to the nearest hundredth.
"""

def convert_to_decimal(arr):
    """
    Converts a list of string digits into a decimal number.
    
    Args:
    arr (list): A list of strings where each string contains only digits from 0 to 9 and has a maximum length of 3 characters.
    
    Returns:
    float: A decimal number rounded to the nearest hundredth.
    """
    # Join the strings and convert to float
    number = float("".join(arr))
    
    # Round to the nearest hundredth
    rounded_number = round(number, 2)
    
    return rounded_number