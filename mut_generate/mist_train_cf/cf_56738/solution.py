"""
QUESTION:
Find a pair of hexadecimal numbers in a sequence that multiply to a given product. The sequence and product will be provided, and you need to write a function named `find_hex_pair` to identify these two numbers.
"""

def find_hex_pair(sequence, product):
    """
    Find a pair of hexadecimal numbers in a sequence that multiply to a given product.

    Args:
        sequence (list): A list of hexadecimal numbers.
        product (int): The target product.

    Returns:
        tuple: A pair of hexadecimal numbers that multiply to the given product, or None if no such pair exists.
    """
    hex_map = {}
    for hex_num in sequence:
        complement = product / int(hex_num, 16)
        if complement.is_integer() and complement in hex_map:
            return (hex_map[complement], hex_num)
        hex_map[int(hex_num, 16)] = hex_num
    return None