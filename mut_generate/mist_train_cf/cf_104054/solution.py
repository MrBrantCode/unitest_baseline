"""
QUESTION:
Write a function `find_maximum_sum` that takes a two-dimensional array of integers as input and returns a list of integers. For each row in the input array, find the maximum sum of any contiguous subarray within that row, handling negative values such that the maximum sum is always a non-negative integer.
"""

def find_maximum_sum(A):
    max_sum = []
    
    for row in A:
        current_sum = 0
        max_subarray_sum = 0
        
        for num in row:
            current_sum += num
            
            if current_sum < 0:
                current_sum = 0
            
            if current_sum > max_subarray_sum:
                max_subarray_sum = current_sum
        
        max_sum.append(max_subarray_sum)
    
    return max_sum