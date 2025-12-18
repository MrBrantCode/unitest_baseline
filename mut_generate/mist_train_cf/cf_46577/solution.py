"""
QUESTION:
Write a function `hex_to_ascii(hex_string)` that converts a given hexadecimal string into its equivalent ASCII characters. The function should take a string of hexadecimal values as input, convert each pair of hexadecimal values into an ASCII character, and return the resulting string. If the input string contains invalid hexadecimal values, the function should catch the corresponding exceptions (`TypeError` and `ValueError`) and handle them gracefully.
"""

def hex_to_ascii(hex_string):
    """
    Converts a given hexadecimal string into its equivalent ASCII characters.

    Args:
    hex_string (str): A string of hexadecimal values.

    Returns:
    str: The resulting ASCII string.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string contains invalid hexadecimal values.
    """
    try:
        # Convert hexadecimal into ASCII
        return "".join([chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2)])
    except (TypeError, ValueError) as e:
        print(f"Invalid input: {e}")
        return None