"""
QUESTION:
Write a function `mergeArrays(arr1, arr2)` that merges two sorted arrays `arr1` and `arr2` in ascending order while removing duplicates and maintaining the original order of the elements. The merged array should have no more than twice the length of the original arrays. The function should return the merged array in descending order. The input arrays are guaranteed to be non-empty and contain only prime numbers.
"""

def mergeArrays(arr1, arr2):
    mergedArr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            if arr1[i] not in mergedArr:
                mergedArr.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            if arr2[j] not in mergedArr:
                mergedArr.append(arr2[j])
            j += 1
        else:
            if arr1[i] not in mergedArr:
                mergedArr.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if arr1[i] not in mergedArr:
            mergedArr.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] not in mergedArr:
            mergedArr.append(arr2[j])
        j += 1

    mergedArr.sort(reverse=True)
    return mergedArr