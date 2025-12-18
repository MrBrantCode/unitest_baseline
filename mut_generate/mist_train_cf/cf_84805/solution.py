"""
QUESTION:
Write a function `max_sum(arr, k)` that finds the highest cumulative total associated with a contiguous subarray of size `k` within a given numerical array `arr`. The function should also return the starting index of this subarray. Ensure to handle edge cases where `k` is larger than the length of the array, `k` is less than 1, or the array is empty.
"""

def max_sum(arr, k):
    # handle edge cases
    if not arr or k > len(arr) or k < 1:
        return "Invalid input"

    current_sum = max_sum = sum(arr[:k])
    starting_index = 0
    for i in range(k,len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            starting_index = i - k + 1
  
    return max_sum, starting_index