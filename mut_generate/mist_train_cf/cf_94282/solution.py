"""
QUESTION:
Implement the `max_subarray_sum` function to find the maximum sum of a subarray in a given array of integers. The subarray can be any length, but it must be non-empty. If the array contains only negative numbers, return the smallest negative number. If multiple subarrays have the same maximum sum, return the sum of the shortest subarray.

The function must meet the following constraints: 
- Time complexity: O(n), where n is the length of the input array.
- Space complexity: O(1), no additional data structures to store intermediate results.
- A single function implementation without using external libraries or built-in functions specifically designed to solve this problem.
- Input array can have negative, zero, or positive integers.
"""

def max_subarray_sum(arr):
    max_sum = float('-inf')  
    current_sum = 0  
    start_index = 0  
    end_index = 0  
    max_length = 1  
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
            max_length = end_index - start_index + 1
        elif current_sum < 0:
            current_sum = 0
            start_index = i + 1
    
    if max_sum < 0:
        return max_sum  
    else:
        return max_sum 