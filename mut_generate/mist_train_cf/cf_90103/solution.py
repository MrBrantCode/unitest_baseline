"""
QUESTION:
Write a function named `calculate_scalar_product` that takes two lists of integers `vector1` and `vector2` as input. The function should return the scalar product of the two vectors if they are in ascending order, otherwise return an error message. If one or both vectors are empty, return 0. The vectors can have a maximum length of 10^6 and must contain only positive integers.
"""

def calculate_scalar_product(vector1, vector2):
    if len(vector1) == 0 or len(vector2) == 0:
        return 0
    
    if vector1 != sorted(vector1) or vector2 != sorted(vector2):
        return "Vectors are not in ascending order"
    
    scalar_product = 0
    for i in range(len(vector1)):
        scalar_product += vector1[i] * vector2[i]
    
    return scalar_product