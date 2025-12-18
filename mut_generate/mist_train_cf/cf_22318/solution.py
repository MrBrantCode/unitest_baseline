"""
QUESTION:
Create a function named `scalar_product` that calculates the scalar product of two vectors. The function should accept two lists of integers as input, where each list represents a vector. The vectors must have the same length, and each element in the vectors must be a positive integer. The function should return 0 if one or both input vectors are empty. If the vectors are not empty, the function should return the sum of the products of corresponding elements in the two vectors. The function should be able to handle vectors of up to 10^6 elements.
"""

def scalar_product(vector1, vector2):
    if len(vector1) == 0 or len(vector2) == 0:
        return 0  # Return 0 if one or both vectors are empty
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    
    return result