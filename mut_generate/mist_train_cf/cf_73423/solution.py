"""
QUESTION:
Write a function named `hex_matrix_sequence_finder` that takes a 2D list of hexadecimal digits and a target product as input, and returns the sequence of digits that, when multiplied together, produces the target product. Assume the input matrix only contains hexadecimal digits and the target product is a non-negative integer. The function should return the first sequence found in row-major order, and if no such sequence exists, return an empty list.
"""

def hex_matrix_sequence_finder(matrix, target_product):
    """
    This function finds the sequence of hexadecimal digits in a given matrix that, 
    when multiplied together, produces the target product.

    Args:
        matrix (list): A 2D list of hexadecimal digits.
        target_product (int): The target product.

    Returns:
        list: The sequence of digits that produces the target product. If no such sequence exists, returns an empty list.
    """

    def is_valid_product(sequence):
        product = 1
        for digit in sequence:
            product *= int(digit, 16)
            if product > target_product:
                return False
        return product == target_product

    def backtrack(row, col, sequence):
        if row == len(matrix):
            return is_valid_product(sequence)

        for i in range(row, len(matrix)):
            for j in range(col if i == row else 0, len(matrix[i])):
                if backtrack(i + (j + 1) // len(matrix[i]), (j + 1) % len(matrix[i]), sequence + [matrix[i][j]]):
                    return True

        return False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if backtrack(i + 1, 0, [matrix[i][j]]):
                return [matrix[i][j]]

    return []