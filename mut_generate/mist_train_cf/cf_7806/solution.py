"""
QUESTION:
Write a function `calculate_scalar_product(vector1, vector2)` that takes two lists of positive integers as input and returns their scalar product. The function should handle the case where one or both vectors are empty by returning 0. It should also check if the input vectors are in ascending order and return a message indicating that they are not if they are not. The function must work for vectors of up to 10^6 elements.
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