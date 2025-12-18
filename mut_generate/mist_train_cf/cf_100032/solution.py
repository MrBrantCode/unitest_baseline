"""
QUESTION:
Create a function `sort_array(arr)` that sorts an array `arr` with non-unique elements in O(n log n) time complexity and O(1) space complexity. The function should return an array of tuples, where each tuple contains the value of an identical element and its first and last index in the sorted array.
"""

def sort_array(arr):
    def partition(low, high):
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


    def modified_quick_sort(low, high):
        if low < high:
            pivot_index, end_index = partition(low, high)
            modified_quick_sort(low, pivot_index - 1)
            modified_quick_sort(end_index + 1, high)


    modified_quick_sort(0, len(arr) - 1)

    output = []
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        output.append((arr[i], i, j - 1))
        i = j

    return output