"""
QUESTION:
Write a function named maxSum that takes two parameters: an array of integers and an integer 'k' representing the size of the subarray. The function should return the maximum aggregated sum of a subarray of size 'k', along with the starting and ending indices of this subarray within the original array. The function should implement the sliding-window algorithm and calculate the sum manually without using built-in functions. If the length of the array is less than 'k', the function should return an error message.
"""

def maxSum(arr, k):
    if len(arr) < k:
        return "Invalid: Array is smaller than window size"
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_index = 0

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_index = i + 1

    return max_sum, max_index, max_index + k - 1