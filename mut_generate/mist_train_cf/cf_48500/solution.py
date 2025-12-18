"""
QUESTION:
Write a function `greater_dot_product` that accepts two sets of three-dimensional numerical vectors as parameters. Each set should contain two vectors, and each vector should be a list of three numbers. The function should calculate the dot product of the vectors in each set, compare the dot products, and return the greater dot product along with the corresponding set of vectors. If the dot products are equal, the function should return all vectors.
"""

def greater_dot_product(set1, set2):
    # Calculate dot products
    dot_product_set1 = sum(i*j for i, j in zip(set1[0], set1[1]))
    dot_product_set2 = sum(i*j for i, j in zip(set2[0], set2[1]))

    # Compare and return greater dot product with corresponding set of vectors
    if dot_product_set1 > dot_product_set2:
        return dot_product_set1, set1
    elif dot_product_set1 < dot_product_set2:
        return dot_product_set2, set2
    else:
        return dot_product_set1, set1, set2