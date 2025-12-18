"""
QUESTION:
Write a function named `find_hex_cluster` that takes two parameters: a string `hex_string` representing a sequence of hexadecimal numbers and an integer `target_product` representing the pre-established result. The function should return a substring of `hex_string` that, when its hexadecimal digits are multiplied together, equals `target_product`. If no such substring exists, return an empty string.
"""

def find_hex_cluster(hex_string, target_product):
    """
    Finds a substring in hex_string where the product of its hexadecimal digits equals target_product.

    Args:
    hex_string (str): A sequence of hexadecimal numbers.
    target_product (int): The pre-established result.

    Returns:
    str: A substring of hex_string that meets the condition, or an empty string if no such substring exists.
    """
    def hex_to_int(hex_char):
        # Convert a hexadecimal character to its integer value
        return int(hex_char, 16)

    for length in range(1, len(hex_string) + 1):
        for i in range(len(hex_string) - length + 1):
            substring = hex_string[i:i + length]
            product = 1
            for char in substring:
                product *= hex_to_int(char)
            if product == target_product:
                return substring

    return ""