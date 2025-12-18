"""
QUESTION:
Implement a function named quicksort that sorts an array of integers in ascending order in-place, without using any extra data structures or libraries, and with an average time complexity of O(nlogn). The function should be able to handle arrays with both duplicate and unique elements. The function should take as input the array and the low and high indices that represent the portion of the array to be sorted.
"""

def partition(arr, low, high):
    pivot = arr[high]  # choose the last element as the pivot
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)