"""
QUESTION:
Implement a function named `merge_sort` that takes an array of unique integers as input and returns a new array with the same integers sorted in ascending order. The function should have a time complexity of O(n log n) and use constant space complexity. Do not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    def merge(left_half, right_half):
        merged_arr = []
        left_index = 0
        right_index = 0

        # Compare elements from both halves and merge them in ascending order
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged_arr.append(left_half[left_index])
                left_index += 1
            else:
                merged_arr.append(right_half[right_index])
                right_index += 1

        # Add any remaining elements from the left half
        while left_index < len(left_half):
            merged_arr.append(left_half[left_index])
            left_index += 1

        # Add any remaining elements from the right half
        while right_index < len(right_half):
            merged_arr.append(right_half[right_index])
            right_index += 1

        return merged_arr

    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged_arr = merge(left_half, right_half)

    return merged_arr