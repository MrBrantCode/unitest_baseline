"""
QUESTION:
Write a function `find_max_subarray_sum(arr)` that takes an array of integers as input and returns the maximum subarray sum that includes at least one negative number and one odd number. The function should return 0 if no such subarray exists or if the input array is empty.
"""

def find_max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    
    for num in arr:
        current_sum += num
        
        if current_sum <= 0:
            current_sum = 0
            
        if current_sum > max_sum:
            max_sum = current_sum
    
    if max_sum == 0:
        return 0
    
    for num in arr:
        if num < 0 and num % 2 != 0:
            return max_sum
    
    return 0