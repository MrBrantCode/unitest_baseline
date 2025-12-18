"""
QUESTION:
Write a function `transpose_array(arr)` that takes a two-dimensional array `arr` with up to 100 rows and 100 columns as input. The function should return the transpose of `arr`, where negative numbers are converted to their absolute values and duplicate elements are removed. If `arr` is empty or contains non-numeric values, the function should return an empty array. Do not use built-in functions or libraries for transposing or removing duplicates.
"""

def transpose_array(arr):
    if not arr or not all(isinstance(x, list) for x in arr):
        return []
    
    if not all(isinstance(element, (int, float)) for row in arr for element in row):
        return []

    transposed_arr = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]

    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if element < 0:
                element = abs(element)
            transposed_arr[j][i] = element

    for i, row in enumerate(transposed_arr):
        transposed_arr[i] = list(set(row))

    return transposed_arr