"""
QUESTION:
Write a function named `compare_arrays` that takes two arrays of integers as input. The function should return a tuple containing two counts: the number of elements that are equal at the same position in both arrays, and the number of elements that are equal but not at the same position in both arrays. The arrays can have a maximum length of 100 and contain integers ranging from -1000 to 1000. The function should handle arrays with duplicate elements correctly and return an error message if the input arrays have different lengths.
"""

def compare_arrays(arr1, arr2):
    same_position_count = 0
    different_position_count = 0
    
    # Check if the lengths of the arrays are equal
    if len(arr1) != len(arr2):
        return "Arrays must have equal length"
    
    # Iterate over the arrays and compare each element
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            same_position_count += 1
        elif arr1[i] in arr2 and arr2.index(arr1[i]) != i:
            different_position_count += 1
    
    return same_position_count, different_position_count