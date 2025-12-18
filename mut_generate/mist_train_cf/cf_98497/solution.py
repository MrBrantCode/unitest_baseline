"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts an array of integers in ascending order, with a time complexity of O(nlogn), where n is the number of elements in the array. The array may contain both positive and negative integers.
"""

def merge_sort(arr):
    def merge(left_arr, right_arr):
        merged = []
        i = 0
        j = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                merged.append(left_arr[i])
                i += 1
            else:
                merged.append(right_arr[j])
                j += 1

        merged += left_arr[i:]
        merged += right_arr[j:]

        return merged

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)