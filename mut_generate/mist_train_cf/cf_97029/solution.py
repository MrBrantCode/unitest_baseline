"""
QUESTION:
Write a function `scalar_product` that takes two lists of integers `vector1` and `vector2` as input and returns their scalar product. The function should handle cases where one or both vectors are empty. The input vectors can have a maximum length of 10^6 and must contain only positive integers.
"""

def scalar_product(vector1, vector2):
    if len(vector1) == 0 or len(vector2) == 0:
        return 0  
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result