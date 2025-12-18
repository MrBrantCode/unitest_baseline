"""
QUESTION:
Implement a function named `quick_sort` that takes an array, a low index, and a high index as input and sorts the array in-place using the quicksort algorithm with a median of three partitioning method for selecting the pivot. The function should be able to handle arrays with repeated elements.
"""

def quick_sort(arr, low, high):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i = i + 1
            while i <= j and arr[j] >= pivot:
                j = j - 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
                
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        if arr[low] < arr[mid]:
            if arr[mid] < arr[high]:
                return mid
            if arr[low] < arr[high]:
                return high
        else:
            if arr[low] < arr[high]:
                return low
            if arr[mid] < arr[high]:
                return high
        return mid

    if low < high:
        mid = median_of_three(arr, low, high)
        arr[low], arr[mid] = arr[mid], arr[low]
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)