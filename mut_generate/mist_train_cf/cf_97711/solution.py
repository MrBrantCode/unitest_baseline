"""
QUESTION:
Create a function `sort_array(arr)` that takes an array of integers as input and returns a list of tuples, where each tuple contains a unique element from the array and its first and last index in the sorted array. The function should have a time complexity of O(n log n) and a space complexity of O(1). The input array contains non-unique elements and should be sorted in-place.
"""

def sort_array(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1
        left_end = low

        while left_end < j:
            if arr[left_end] < pivot:
                i += 1
                arr[left_end], arr[i] = arr[i], arr[left_end]
                left_end += 1
            elif arr[left_end] > pivot:
                j -= 1
                arr[left_end], arr[j] = arr[j], arr[left_end]
            else:
                left_end += 1

        return i + 1, j - 1


    def modified_quick_sort(arr, low, high):
        if low < high:
            pivot_index, end_index = partition(arr, low, high)
            modified_quick_sort(arr, low, pivot_index - 1)
            modified_quick_sort(arr, end_index + 1, high)

    modified_quick_sort(arr, 0, len(arr) - 1)

    output = []
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        output.append((arr[i], i, j - 1))
        i = j

    return output