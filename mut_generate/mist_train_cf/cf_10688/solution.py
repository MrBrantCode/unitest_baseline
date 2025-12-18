"""
QUESTION:
Implement a function named `sort_array_descending` that sorts a linear array in descending order using a variation of quicksort. The function should sort the array in-place without using any additional data structures, have a time complexity of O(nlogn), and a space complexity of O(logn). The function should also correctly handle arrays containing duplicate elements.
"""

def sort_array_descending(arr):
    def partition(low, high):
        pivot = arr[high]  
        i = low - 1  

        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    quicksort(0, len(arr) - 1)