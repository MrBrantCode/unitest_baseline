"""
QUESTION:
Implement the `max_sum_subarray` function that takes an array of integers as input and returns the maximum sum of all possible subarrays. If the array contains all negative elements, the function should return the maximum among them. The function should have a time complexity of O(n), where n is the number of elements in the input array.
"""

def max_sum_subarray(arr):
    if max(arr) < 0:  
        return max(arr)

    max_sum = current_sum = 0  
    for num in arr:  
        current_sum += num  
        if current_sum < 0:  
            current_sum = 0  
        max_sum = max(max_sum, current_sum)  
    return max_sum