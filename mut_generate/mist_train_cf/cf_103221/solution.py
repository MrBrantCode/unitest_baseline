"""
QUESTION:
Write a function named `compare_arrays` that takes two arrays `arr1` and `arr2` as input and returns a boolean indicating whether the two arrays are equal and the count of elements that are equal at the same position in both arrays. The function should return False immediately if the lengths of the two arrays are not equal.
"""

def entance(arr1, arr2):
    equal_count = 0
    # Check if the lengths of the arrays are equal
    if len(arr1) != len(arr2):
        return False, equal_count
    
    # Iterate over the arrays and compare elements at the same position
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            equal_count += 1
    
    return equal_count == len(arr1), equal_count