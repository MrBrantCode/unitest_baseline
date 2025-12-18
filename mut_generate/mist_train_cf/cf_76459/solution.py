"""
QUESTION:
Write a function `hex_matrix_sequence` that, given a matrix of hexadecimal digits and a target product, finds and returns a sequence of digits in the matrix that, when multiplied together, produce the target product.
"""

from itertools import product

def hex_matrix_sequence(matrix, target_product):
    """
    This function finds and returns a sequence of digits in the matrix that, 
    when multiplied together, produce the target product.

    Args:
    matrix (list): A 2D list of hexadecimal digits.
    target_product (int): The target product.

    Returns:
    list or None: A list of digits that multiply to the target product, or None if no such sequence exists.
    """

    # Generate all possible sequences of digits from the matrix
    sequences = list(product(*matrix))

    # Iterate over each sequence
    for sequence in sequences:
        # Convert each digit from hexadecimal to integer
        digits = [int(digit, 16) for digit in sequence]
        
        # Calculate the product of the digits
        product_of_digits = 1
        for digit in digits:
            product_of_digits *= digit

        # Check if the product of the digits equals the target product
        if product_of_digits == target_product:
            return list(sequence)

    # If no sequence is found, return None
    return None