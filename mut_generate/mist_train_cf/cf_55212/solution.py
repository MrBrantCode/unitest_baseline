"""
QUESTION:
Write a function `array_mult(array1, array2)` that calculates the element-wise multiplication of two 1D arrays. The function should return a new array where each element is the product of the corresponding elements from the two input arrays. If the input arrays are not the same length, the function should return an error message.
"""

def array_mult(array1, array2):
    if len(array1) != len(array2):
        return "Arrays are not the same length"
    else:
        return [array1[i]*array2[i] for i in range(len(array1))]