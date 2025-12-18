"""
QUESTION:
Create a function named `cumulative_product_hex_to_dec` that takes a list of hexadecimal strings as input. Convert each hexadecimal string to its decimal equivalent and compute the cumulative product of these decimal numbers. The function should return the final cumulative product. The input list may contain both hexadecimal letters (A-F) and numeric characters (0-9).
"""

def cumulative_product_hex_to_dec(hex_strings):
    """
    This function takes a list of hexadecimal strings, converts each to decimal, 
    and computes the cumulative product of these decimal numbers.

    Args:
    hex_strings (list): A list of hexadecimal strings.

    Returns:
    int: The cumulative product of the decimal equivalents of the input hexadecimal strings.
    """
    # Initialize the cumulative product to 1
    cumulative_product = 1
    
    # Iterate over each hexadecimal string in the input list
    for hex_string in hex_strings:
        # Convert the hexadecimal string to decimal and multiply it with the cumulative product
        cumulative_product *= int(hex_string, 16)
    
    # Return the final cumulative product
    return cumulative_product