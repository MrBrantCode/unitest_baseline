"""
QUESTION:
Write a function called `find_hex_product` that takes a list of hexadecimal numbers and a target product as input. The function should find two hexadecimal numbers from the list that, when multiplied together, yield the target product and return these two numbers.
"""

def find_hex_product(hex_numbers, target_product):
    """
    This function finds two hexadecimal numbers from the list that, when multiplied together, yield the target product.

    Parameters:
    hex_numbers (list): A list of hexadecimal numbers.
    target_product (int): The target product.

    Returns:
    tuple: A tuple containing two hexadecimal numbers that yield the target product when multiplied together. If no pair is found, returns None.
    """
    for i in range(len(hex_numbers)):
        for j in range(i + 1, len(hex_numbers)):
            if int(hex_numbers[i], 16) * int(hex_numbers[j], 16) == target_product:
                return (hex_numbers[i], hex_numbers[j])
    return None