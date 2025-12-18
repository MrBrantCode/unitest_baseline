"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers `arr` and a positive integer `k` as input. The function should return the maximum sum of a subarray within `arr` with a length of at least `k`. The function should have a time complexity of O(n), where n is the length of the input array. If `k` is greater than the length of the array, the function should return 0.
"""

def entrance(arr, k):
    n = len(arr)
    
    # If k is greater than the length of the array, return 0
    if k > n:
        return 0
    
    max_sum = float('-inf')
    curr_sum = 0
    
    # Initialize the current sum by summing the first k elements
    for i in range(k):
        curr_sum += arr[i]
    
    # Iterate through the array, updating the current sum and max sum
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]  # Update the current sum by adding the next element and subtracting the first element of the previous subarray
        max_sum = max(max_sum, curr_sum)  # Update the max sum if necessary
    
    return max_sum