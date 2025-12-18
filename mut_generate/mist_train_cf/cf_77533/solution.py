"""
QUESTION:
Implement a function `insertionSort` that takes an array of integers and a string `order` as input, where `order` is either 'asc' or 'desc'. The function should perform a stable insertion sort on the array in the specified order and return the sorted array. After sorting, the function should also remove any duplicate values from the array, maintaining the relative order of equal elements.
"""

def insertionSort(arr, order):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if order == "desc":
            while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result