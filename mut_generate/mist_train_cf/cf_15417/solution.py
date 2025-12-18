"""
QUESTION:
Write a function `optimized_sort(arr)` that takes an array `arr` as input, removes any duplicate elements, and returns a new array with the remaining elements sorted in ascending order. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def optimized_sort(arr):
    # Remove duplicates from the array
    arr = list(set(arr))
    
    # Merge sort implementation
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)

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

    # Sort the array using merge sort
    sorted_arr = merge_sort(arr)
    
    return sorted_arr