"""
QUESTION:
Given a list of phone numbers in string format, write a function `find_max_phone_number` that returns the phone number with the maximum numerical value. The phone numbers are prefixed with '+' and may have leading zeros. The function should ignore the '+' and leading zeros when comparing the numerical values.
"""

def find_max_phone_number(phone_numbers):
    """
    Returns the phone number with the maximum numerical value.
    
    Args:
    phone_numbers (list): A list of phone numbers in string format.
    
    Returns:
    str: The phone number with the maximum numerical value.
    """
    # Remove the '+' and '0' in the beginning and convert strings into integers
    phone_numbers_as_int = [int(phone_number.replace("+", "")[1:]) for phone_number in phone_numbers]
    
    # Find the maximum
    max_value = max(phone_numbers_as_int)
    
    # Find the initial phone number string with the maximum value
    max_phone_number = phone_numbers[phone_numbers_as_int.index(max_value)]
    
    return max_phone_number