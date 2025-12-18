"""
QUESTION:
Create a function `mergeSort(arr, left, right)` that sorts the subarray `arr[left...right]` in descending order. The function should have a time complexity of O(n log n) and should be able to handle arrays with duplicate elements. The function should modify the original array in-place.
"""

def mergeSort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    leftArr = arr[left:mid+1]
    rightArr = arr[mid+1:right+1]
    i = j = 0
    k = left

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] >= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1