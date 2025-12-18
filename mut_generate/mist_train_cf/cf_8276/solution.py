"""
QUESTION:
Write a function `find_common_elements` that takes two arrays of integers as input, and returns an array of integers that are common to both input arrays. The returned array should be in ascending order and should not contain any duplicates. The function should have a time complexity less than O(n), where n is the length of the longer array, and should not use any additional data structures such as hash maps or sets.
"""

def find_common_elements(arr1, arr2):
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