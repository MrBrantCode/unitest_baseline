"""
QUESTION:
Implement a function called `sort_list` that takes a list of integers as input, sorts it in ascending order using constant space and without built-in sorting functions, and returns the sorted list along with the number of swaps performed during the sorting process. The function should handle duplicate integers, negative integers, and large input lists with up to 10^6 elements efficiently, with a time complexity of O(n log n) and constant space complexity.
"""

def sort_list(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        swaps = 0

        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[low], arr[j] = arr[j], arr[low]
        swaps += 1

        return j, swaps


    def quicksort(arr, low, high):
        swaps = 0

        if low < high:
            pivot_index, swaps = partition(arr, low, high)

            left_swaps = quicksort(arr, low, pivot_index - 1)
            right_swaps = quicksort(arr, pivot_index + 1, high)

            swaps += left_swaps + right_swaps

        return swaps


    swaps = quicksort(arr, 0, len(arr) - 1)
    return arr, swaps