"""
QUESTION:
Create a function `mergeSort(arr)` that takes an array of integers as input and returns a new array with the elements sorted in ascending order. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions, recursion, or additional data structures except for the given array. The function should handle duplicate elements correctly and place them in the correct order.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    sortedArr = []
    i = j = 0

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArr.append(leftHalf[i])
            i += 1
        else:
            sortedArr.append(rightHalf[j])
            j += 1

    while i < len(leftHalf):
        sortedArr.append(leftHalf[i])
        i += 1

    while j < len(rightHalf):
        sortedArr.append(rightHalf[j])
        j += 1

    return sortedArr