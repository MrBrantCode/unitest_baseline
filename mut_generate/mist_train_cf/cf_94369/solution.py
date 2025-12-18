"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input, sorts them in descending order, and prints the sorted array. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n log n) or better.
"""

def sort_array(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1
        
        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1
        
        return merged
    
    sorted_arr = merge_sort(arr)
    for num in sorted_arr:
        print(num)