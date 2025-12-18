"""
QUESTION:
Write a function `max_sum_subarray` that takes an array of integers as input and returns the maximum sum that can be obtained from a non-contiguous subarray. The function should handle arrays of any length, including empty arrays and arrays with a single element.
"""

def max_sum_subarray(arr):
    n = len(arr)
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    # Initialize two variables to store the maximum sum
    include = arr[0]
    exclude = 0
    
    # Iterate through the array
    for i in range(1, n):
        # Update the maximum sum by including or excluding the current element
        new_include = exclude + arr[i]
        new_exclude = max(include, exclude)
        
        # Update the include and exclude variables
        include = new_include
        exclude = new_exclude
    
    # Return the maximum sum
    return max(include, exclude)