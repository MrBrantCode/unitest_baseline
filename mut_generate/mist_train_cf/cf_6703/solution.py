"""
QUESTION:
Write a Python function `find_max_subarray_sum` that takes an array of integers as input and returns the maximum subarray sum, which is the sum of the largest possible contiguous subarray within the array. The array can contain both positive and negative integers and may be empty. The solution should have a time complexity of O(n), where n is the length of the array, and should be implemented without using any loops, recursion, built-in functions, or extra space for variables or arrays.
"""

def find_max_subarray_sum(nums):
    if not nums:  
        return 0
    
    # Initialize variables
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        # Calculate the maximum subarray sum ending at the current element
        current_sum = max(num, current_sum + num)
        
        # Update the maximum subarray sum seen so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum