"""
QUESTION:
Write a function named `dot_product` that takes two arrays of numbers as input and returns their dot product. The input arrays may contain non-integer elements and must have the same length. If the arrays do not have the same length, the function should return an error message.
"""

def dot_product(array1, array2):
    if len(array1) != len(array2):
        return "Arrays must have the same length."
    
    result = 0
    for i in range(len(array1)):
        result += array1[i] * array2[i]
    
    return result