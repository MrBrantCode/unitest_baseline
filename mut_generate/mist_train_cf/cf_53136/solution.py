"""
QUESTION:
Create a function named `alternate_arrays` that accepts three numeric arrays `arr1`, `arr2`, and `arr3` as input. The function should produce a single output array containing the elements of the three input arrays alternately, starting with the first array. The output array should include all elements from the input arrays, even if they have different lengths.
"""

def alternate_arrays(arr1, arr2, arr3):
    output = []
    for i in range(max(len(arr1), len(arr2), len(arr3))):
        if i < len(arr1):
            output.append(arr1[i])
        if i < len(arr2):
            output.append(arr2[i])
        if i < len(arr3):
            output.append(arr3[i])
    return output