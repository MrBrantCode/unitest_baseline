"""
QUESTION:
Write a function named `max_subarray_sum` that takes an array of integers and an integer `k` as input, and returns the subarray with the maximum sum less than `k`. The function should return the subarray that has the maximum sum while still being less than `k`. If no such subarray exists, the function may return an empty array or a message indicating that no subarray was found.
"""

def max_subarray_sum(arr, k):
    max_sum = 0 
    start = 0 
    end = 0

    for i in range(len(arr)): 
        sum = 0
        for j in range(i, len(arr)): 
            sum += arr[j] 
            if (sum > max_sum and sum <= k): 
                max_sum = sum 
                start = i 
                end = j 
    if max_sum != 0:
        return arr[start:end+1]
    else:
        return "No subarray found"