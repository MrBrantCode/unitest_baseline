"""
QUESTION:
Find the specific set of hexadecimal digits within a sequence that, when multiplied together, produce a predetermined result. Write a function `find_hex_digits` that takes a sequence of hexadecimal digits and a target product as input.
"""

from itertools import combinations

def find_hex_digits(hex_sequence, target_product):
    """
    Find a set of hexadecimal digits in a sequence that, when multiplied together, produce a target product.

    Args:
    hex_sequence (str): A sequence of hexadecimal digits.
    target_product (int): The target product.

    Returns:
    tuple: A tuple of hexadecimal digits that, when multiplied together, produce the target product.
    """

    # Convert the hexadecimal sequence to a list of integers
    hex_ints = [int(digit, 16) for digit in hex_sequence]

    # Iterate over all possible combinations of the hexadecimal digits
    for r in range(1, len(hex_sequence) + 1):
        for combination in combinations(hex_ints, r):
            # Check if the product of the current combination equals the target product
            if eval('*'.join(map(str, combination))) == target_product:
                # If a match is found, return the combination as a tuple of hexadecimal digits
                return tuple(hex(digit)[2:] for digit in combination)

    # If no match is found, return None
    return None