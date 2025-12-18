"""
QUESTION:
Write a function named `vector_addition` that takes two 1D arrays as input and returns their element-wise sum. If the arrays have different lengths, the function should append the remaining elements of the longer array to the result. The resulting array should be returned in reverse order.
"""

def vector_addition(array1, array2):
    result = []
    if len(array1) > len(array2):
        for i in range(len(array1)):
            if i < len(array2):
                result.append(array1[i] + array2[i])
            else:
                result.append(array1[i])
    elif len(array1) < len(array2):
        for i in range(len(array2)):
            if i < len(array1):
                result.append(array1[i] + array2[i])
            else:
                result.append(array2[i])
    else:
        for i in range(len(array1)):
            result.append(array1[i] + array2[i])
    return result[::-1]