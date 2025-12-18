"""
QUESTION:
Write a function `find_maximum_sum` that takes a two-dimensional array of integers `A` as input. The function should return a list of maximum sum of any subarray within each row in `A`. A subarray is defined as a contiguous block of elements in the same row. Ensure that the maximum sum is always a non-negative integer by handling any negative values in the array.
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