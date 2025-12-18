"""
QUESTION:
Write a function called `merge_arrays` that takes two sorted arrays `arr1` and `arr2` as input and returns a new sorted array. The function should merge the input arrays into a new array of size n + m, where n and m are the sizes of `arr1` and `arr2` respectively. The function should have a time complexity of O(n + m) and should not use any additional data structures or allocate additional space, except for the output array. The input arrays are sorted in ascending order and may contain duplicates, which should be handled correctly in the merged array.
"""

def merge_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    mergedArray = [0] * (n + m)
    index1 = 0
    index2 = 0
    indexMerged = 0
    
    while index1 < n and index2 < m:
        if arr1[index1] <= arr2[index2]:
            mergedArray[indexMerged] = arr1[index1]
            index1 += 1
        else:
            mergedArray[indexMerged] = arr2[index2]
            index2 += 1
        indexMerged += 1
    
    while index1 < n:
        mergedArray[indexMerged] = arr1[index1]
        index1 += 1
        indexMerged += 1
    
    while index2 < m:
        mergedArray[indexMerged] = arr2[index2]
        index2 += 1
        indexMerged += 1
    
    return mergedArray