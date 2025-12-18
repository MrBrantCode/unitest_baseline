"""
QUESTION:
Implement a function called `quickSort` that takes an array `arr`, a starting index `low`, and an ending index `high` as input. The function should sort the array using an adaptive quicksort algorithm, where the pivot is chosen as the median of the first, middle, and last numbers in the array. The function should be able to handle any array of integers, not just the example input.
"""

def quickSort(arr, low, high):
    def get_pivot(arr, low, high):
        mid = (high + low) // 2
        pivot = high
        if arr[low] < arr[mid]:
            if arr[mid] < arr[high]:
                pivot = mid
        elif arr[low] < arr[high]:
            pivot = low
        return pivot
    
    def partition(arr, low, high):
        i = (low-1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    if len(arr) == 1:
        return arr
    if low < high:
        pivot_index = get_pivot(arr, low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index-1)
        quickSort(arr, pivot_index+1, high)