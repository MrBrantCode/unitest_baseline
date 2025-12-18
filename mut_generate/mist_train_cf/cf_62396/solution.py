"""
QUESTION:
Find a specific group of hexadecimal digits in a sequence whose product equals a predefined number. The function should be named 'find_hex_group'. The function should take two parameters: a string of hexadecimal digits and a target product. The function should return the first sequence of hexadecimal digits that, when multiplied, equals the target product.
"""

def find_hex_group(hex_string, target_product):
    """
    Find a specific group of hexadecimal digits in a sequence whose product equals a predefined number.

    Args:
        hex_string (str): A string of hexadecimal digits.
        target_product (int): The target product.

    Returns:
        str: The first sequence of hexadecimal digits that, when multiplied, equals the target product.
    """

    def hex_to_int(hex_str):
        # Convert a hexadecimal string to an integer
        return int(hex_str, 16)

    def is_valid_product(hex_str):
        # Check if the product of hexadecimal digits in a string equals the target product
        product = 1
        for digit in hex_str:
            product *= hex_to_int(digit)
        return product == target_product

    window_size = 1
    while window_size <= len(hex_string):
        for i in range(len(hex_string) - window_size + 1):
            # Get the current window of hexadecimal digits
            window = hex_string[i:i + window_size]
            # Check if the product of the current window equals the target product
            if is_valid_product(window):
                return window
        window_size += 1
    return None