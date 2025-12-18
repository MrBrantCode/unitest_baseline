"""
QUESTION:
Write a function `smallest_subarray_with_sum` that finds the length of the smallest contiguous subarray in the input array that has a sum greater than or equal to the target sum. If no such subarray exists, the function should return -1.

The function takes two inputs: an array of integers and a target sum. The function must have a time complexity of O(n), where n is the length of the input array, and use constant space. If there are multiple subarrays with the same smallest length, the function should return the subarray with the maximum sum.
"""

def smallest_subarray_with_sum(arr, target):
    n = len(arr)
    min_length = float('inf') 
    start = 0
    end = 0
    current_sum = 0
    
    while end < n:
        current_sum += arr[end]
        
        while current_sum >= target:
            min_length = min(min_length, end - start + 1) 
            current_sum -= arr[start]
            start += 1
        
        end += 1
    
    return min_length if min_length != float('inf') else -1