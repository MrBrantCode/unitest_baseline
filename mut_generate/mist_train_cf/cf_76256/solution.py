"""
QUESTION:
Write a function `find_hex_digits` that takes a sequence of hexadecimal digits and a target product as input. Return the first set of contiguous hexadecimal digits in the sequence that, when multiplied together, yield the target product.
"""

def find_hex_digits(hex_sequence, target_product):
    """
    Finds the first set of contiguous hexadecimal digits in the sequence 
    that, when multiplied together, yield the target product.

    Args:
    hex_sequence (str): A sequence of hexadecimal digits.
    target_product (int): The target product.

    Returns:
    str: The first set of contiguous hexadecimal digits that yield the target product.
    """
    
    def hex_to_int(hex_str):
        """Converts a hexadecimal string to an integer."""
        return int(hex_str, 16)

    product = 1
    for length in range(1, len(hex_sequence) + 1):
        for i in range(len(hex_sequence) - length + 1):
            substring = hex_sequence[i:i+length]
            product = hex_to_int(substring)
            if product == target_product:
                return substring
    return None