"""
QUESTION:
Write a function `merge_sort(arr)` that implements the merge sort algorithm to sort an array of integers in ascending order. The function should be efficient in terms of time and space complexity. Analyze the time and space complexity of the function using Big O notation.
"""

def merge_sort(arr):
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged += left[left_index:]
        merged += right[right_index:]
        return merged

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))