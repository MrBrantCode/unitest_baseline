"""
QUESTION:
Write a function `cumulative_sum_except_self` that takes an array of integers as input and returns a new array. In the new array, each element at index `i` should be the sum of all elements in the original array except the element at index `i`. The function should only use a single pass through the input array to calculate the total sum.
"""

def cumulative_sum_except_self(arr):
    total_sum = sum(arr)
    return [total_sum - num for num in arr]