"""
QUESTION:
Implement a function `recursiveSort(arr)` that recursively sorts an array of elements in ascending order. The function should handle base cases where the input array is empty or contains only one element without making any unnecessary recursive calls.
"""

def recursiveSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    leftArr = []
    rightArr = []

    for element in arr[1:]:
        if element <= pivot:
            leftArr.append(element)
        else:
            rightArr.append(element)

    sortedLeftArr = recursiveSort(leftArr)
    sortedRightArr = recursiveSort(rightArr)

    return sortedLeftArr + [pivot] + sortedRightArr