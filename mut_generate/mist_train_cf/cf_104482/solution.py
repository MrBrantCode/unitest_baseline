"""
QUESTION:
Compare two arrays of equal length for equality and determine the number of elements that are equal at the same position in both arrays and the number of elements that are equal but not at the same position in both arrays. Write a function called `compare_arrays` that takes two arrays as input and returns a tuple of two counts: the count of equal elements at the same position and the count of equal elements but not at the same position.
"""

def compare_arrays(arr1, arr2):
    same_position_count = 0
    different_position_count = 0

    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            same_position_count += 1
        elif arr1[i] in arr2:
            different_position_count += 1

    return same_position_count, different_position_count