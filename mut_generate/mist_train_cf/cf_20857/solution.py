"""
QUESTION:
Write a function named `cumulative_sum` that calculates the cumulative sum of an array while skipping the first two elements. The function should take an array as input and return the cumulative sum array. The input array should have at least 3 elements; otherwise, the function should return an error message.
"""

def entrance(arr):
    if len(arr) < 3:
        return "Array should have at least 3 elements"
    
    cumulative_sum = [0] * len(arr)
    cumulative_sum[2] = arr[2]

    for i in range(3, len(arr)):
        cumulative_sum[i] = cumulative_sum[i-1] + arr[i]

    return cumulative_sum