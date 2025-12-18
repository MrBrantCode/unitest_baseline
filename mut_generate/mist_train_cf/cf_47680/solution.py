"""
QUESTION:
Write a function `merge_sort(arr)` that takes an array of integers as input and returns a sorted array using the Merge Sort algorithm. The function should recursively split the array into two halves until each half contains only one element, and then merge the halves back together in sorted order.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = int(len(arr) / 2)
    left_half, right_half = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    def merge(left_half, right_half):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1
                
        merged.extend(left_half[left_index:])
        merged.extend(right_half[right_index:])
        return merged

    return merge(left_half, right_half)