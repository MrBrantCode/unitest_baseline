"""
QUESTION:
Implement a function called `max_subarray_sum` that takes an array of integers as input and returns the maximum subarray sum. The function should have a time complexity of O(n), where n is the number of elements in the array, and use a constant amount of space. The subarray must consist of at least one element, and the function should handle negative numbers in the array and not modify the original array.
"""

def max_subarray_sum(arr):
    max_sum = arr[0]  
    current_sum = arr[0]  

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum