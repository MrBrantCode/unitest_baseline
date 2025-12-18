"""
QUESTION:
Write a function named `hex_sequence_multiplier` that takes two parameters: a 2D list of hexadecimal digits and a target product. The function should return the sequence of hexadecimal digits from the 2D list that, when multiplied together, equals the target product.
"""

def hex_sequence_multiplier(hex_matrix, target_product):
    """
    This function finds the sequence of hexadecimal digits from a given 2D list that, 
    when multiplied together, equals a target product.

    Args:
    hex_matrix (list): A 2D list of hexadecimal digits.
    target_product (int): The target product to be achieved.

    Returns:
    list: The sequence of hexadecimal digits that, when multiplied together, equals the target product.
    """
    
    def backtrack(index, current_product, current_sequence):
        if current_product == target_product:
            return current_sequence
        if current_product > target_product or index == len(hex_matrix):
            return None
        
        for i in range(index, len(hex_matrix)):
            for j in range(len(hex_matrix[i])):
                next_product = current_product * int(hex_matrix[i][j], 16)
                next_sequence = current_sequence + [hex_matrix[i][j]]
                result = backtrack(i + 1, next_product, next_sequence)
                if result is not None:
                    return result
        return None

    return backtrack(0, 1, [])