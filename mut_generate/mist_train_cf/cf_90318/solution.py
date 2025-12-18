"""
QUESTION:
Write a function named `find_common_elements` that takes two arrays of integers as input. The function should return the common elements of the two arrays in ascending order, without any duplicates. The time complexity of the solution should be less than or equal to O(n), where n is the length of the longer array, and no additional data structures such as hash maps or sets should be used.
"""

def entrance(arr1, arr2):
    arr1.sort()
    arr2.sort()

    result = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] == arr2[pointer2]:
            if len(result) == 0 or arr1[pointer1] != result[-1]:
                result.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif arr1[pointer1] < arr2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1

    return result