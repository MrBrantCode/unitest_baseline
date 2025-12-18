"""
QUESTION:
Implement a function called max_subarray_sum that takes an array of integers as input and returns the maximum sum of a non-empty subarray. If the array contains only negative numbers, return the smallest negative number. If multiple subarrays have the same maximum sum, return the sum of the subarray with the smallest length. The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def max_subarray_sum(arr):
    max_sum = float('-inf')  
    current_sum = 0  
    min_length = float('inf')  
    current_length = 0  
    
    for i in range(len(arr)):
        current_sum += arr[i]
        current_length += 1
        
        if current_sum > max_sum:
            if current_length < min_length:
                max_sum = current_sum
                min_length = current_length
        elif current_sum < 0:
            current_sum = 0
            current_length = 0
    
    if max_sum < 0:
        return max(arr)  # Return the smallest negative number if all elements are negative
    else:
        return max_sum  # Return the maximum sum of the subarray