"""
QUESTION:
Write a function `find_maximum_subarray_sum(array)` that finds the maximum subarray sum in a given array and returns the indices of the subarray that has the maximum sum. The function should handle edge cases such as when the array is empty or contains only negative numbers, and should have a time complexity of O(n) without using any extra space.
"""

def find_maximum_subarray_sum(array):
    max_sum = 0
    current_sum = 0
    start_index = -1
    end_index = -1
    
    if len(array) == 0:
        return start_index, end_index
    
    for i in range(len(array)):
        current_sum += array[i]
        
        if current_sum < 0:
            current_sum = 0
            start_index = i + 1
        
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
    
    if max_sum == 0:
        max_negative = max(array)
        start_index = array.index(max_negative)
        end_index = start_index
    
    return start_index, end_index