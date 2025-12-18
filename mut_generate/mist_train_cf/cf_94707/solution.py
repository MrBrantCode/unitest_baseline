"""
QUESTION:
Write a function called `mergeArrays` that merges two sorted arrays `arr1` and `arr2` in ascending order, removes duplicates, and maintains the original order of elements. The function should then reverse the merged array to sort it in descending order. The input arrays are guaranteed to be non-empty and contain only unique or duplicate prime numbers. The merged array should have no more than twice the length of the original arrays. The function should return the merged array.
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

    # Append remaining elements from the first array
    while i < len(arr1):
        if arr1[i] not in mergedArr:
            mergedArr.append(arr1[i])
        i += 1

    # Append remaining elements from the second array
    while j < len(arr2):
        if arr2[j] not in mergedArr:
            mergedArr.append(arr2[j])
        j += 1

    mergedArr.sort(reverse=True)
    return mergedArr