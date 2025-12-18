"""
QUESTION:
Design a function `sparse_dot_product` that calculates the scalar product of two n-dimensional sparse vectors. The input vectors are represented as lists of tuples, where each tuple contains the position and value of a non-zero entry in the vector. The function should exploit the sparsity of the vectors to minimize computational resources. Assume that the positions in the input vectors are unique.
"""

def sparse_dot_product(vec1, vec2):
    """
    Calculate the scalar product of two n-dimensional sparse vectors.

    Args:
        vec1 (list[tuple]): The first sparse vector represented as a list of tuples.
        vec2 (list[tuple]): The second sparse vector represented as a list of tuples.

    Returns:
        int: The scalar product of the two input vectors.
    """

    # Convert the input vectors into dictionaries for efficient lookups
    dict1 = {pos: val for pos, val in vec1}
    dict2 = {pos: val for pos, val in vec2}
    
    # Initialize the sum of the products
    product_sum = 0
    
    # Iterate over the common positions in both vectors
    for k in set(dict1.keys()).intersection(dict2.keys()):
        # Multiply the values at the common positions and add to the sum
        product_sum += dict1[k] * dict2[k]

    return product_sum