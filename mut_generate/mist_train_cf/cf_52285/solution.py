"""
QUESTION:
Implement a function `find_common_elements(arr1, arr2)` that finds elements that exist in both input arrays `arr1` and `arr2`, both of which are sorted. The function should not use built-in intersect functions and should have a time complexity lower than O(n^2).
"""

def find_common_elements(arr1, arr2):
    i, j = 0, 0
    common_elements = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
            
    return common_elements