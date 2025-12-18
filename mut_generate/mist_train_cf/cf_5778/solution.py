"""
QUESTION:
Implement a function called `max_subarray_sum` that takes an array of integers as input and returns the maximum subarray sum, where the subarray must consist of at least one element. The function should have a time complexity of O(n), where n is the number of elements in the array, and use a constant amount of space. The function should not modify the original array and should handle arrays containing negative numbers.
"""

def max_subarray_sum(arr):
    max_sum = arr[0]  # Initialize max_sum with the first element of the array
    current_sum = arr[0]  # Initialize current_sum with the first element of the array

    for i in range(1, len(arr)):
        # Calculate the maximum sum ending at the current element
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update the maximum sum so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum