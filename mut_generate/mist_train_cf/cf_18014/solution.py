"""
QUESTION:
Write a function called hex_to_binary that takes a string representing a hexadecimal number as input and returns the binary representation of the decimal equivalent as a string. The function should handle both uppercase and lowercase letters, and it should validate the input to ensure that it only contains hexadecimal digits (0-9, A-F, a-f). If the input is not a valid hexadecimal number, the function should return an error message.
"""

def hex_to_binary(hex_value):
    """
    Convert a hexadecimal number to its binary representation.

    Args:
        hex_value (str): A string representing a hexadecimal number.

    Returns:
        str: The binary representation of the decimal equivalent of the input hexadecimal number.
        str: An error message if the input is not a valid hexadecimal number.
    """

    try:
        # Convert the hexadecimal value to its decimal equivalent
        decimal_value = int(hex_value, 16)
        
        # Convert the decimal value to binary and return it
        return bin(decimal_value)[2:]
    except ValueError:
        # Return an error message if the input is not a valid hexadecimal value
        return "Error: Invalid hexadecimal value"