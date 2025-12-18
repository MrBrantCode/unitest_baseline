"""
QUESTION:
Write a function `max_sum_neg_odd(arr, i, curr_sum, max_sum)` that uses recursion to calculate the highest sum of consecutively appearing negative numbers in an array, but only considers negative numbers in odd-indexed positions. The function should take four parameters: the input array `arr`, the current index `i`, the current sum of negative numbers `curr_sum`, and the maximum sum found so far `max_sum`. If `i` exceeds the array length, the function should return `max_sum`.
"""

def max_sum_neg_odd(arr, i=1, curr_sum=0, max_sum=-float('inf')):
    if i >= len(arr):
        # base case
        return max_sum
    if arr[i] < 0 and i % 2 != 0:
        # if the current number is negative and in an odd-indexed position, add it to the current sum
        curr_sum += arr[i]
        if curr_sum > max_sum:
            # if the current sum is greater than the max sum, update the max sum
            max_sum = curr_sum
    else:
        # if the current number is not negative or is in an even-indexed position, reset the current sum
        curr_sum = 0
    # recursively call the function for the next index
    return max_sum_neg_odd(arr, i+1, curr_sum, max_sum)