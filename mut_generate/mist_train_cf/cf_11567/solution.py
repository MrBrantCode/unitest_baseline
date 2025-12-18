"""
QUESTION:
Create a function named `decimal_to_hexadecimal` that takes one parameter, a decimal number as a string, and returns its corresponding hexadecimal value as a string. The function should handle cases where the input is not a valid decimal number and return "Invalid decimal number" in such cases. The hexadecimal value should not include the '0x' prefix.
"""

def decimal_to_hexadecimal(decimal):
    try:
        # Convert decimal to hexadecimal using built-in hex() function
        hexadecimal = hex(int(decimal))
        return hexadecimal[2:]  # Remove '0x' prefix from hexadecimal value
    except ValueError:
        return "Invalid decimal number"