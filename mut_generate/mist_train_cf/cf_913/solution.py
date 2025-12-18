"""
QUESTION:
Write a function called "convertToValidString" that takes an integer as input and returns a string. The input integer must be within the range of 1 to 1000000 (inclusive) and the output string should contain only numeric characters and have a length of exactly 10 digits. If the input is outside the specified range, return an error message.
"""

def convertToValidString(n):
    """
    Converts an integer to a 10-digit numeric string.
    
    Args:
    n (int): The input integer to be converted. It must be within the range of 1 to 1000000 (inclusive).
    
    Returns:
    str: A 10-digit numeric string representation of the input integer. If the input is outside the specified range, returns an error message.
    """
    if not 1 <= n <= 1000000:
        return "Error: Input is outside the range of 1 to 1000000."
    
    # Convert the number to a string and add leading zeros if necessary
    return str(n).zfill(10)