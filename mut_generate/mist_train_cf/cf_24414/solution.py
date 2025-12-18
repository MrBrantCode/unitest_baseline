"""
QUESTION:
Write a function `cumulative_sum` that takes an array of integers as input and returns a new array where each element at index `i` is the sum of all elements in the original array up to and including index `i`.
"""

def cumulative_sum(arr):
    cum_sum = []
    temp_sum = 0
    for num in arr:
        temp_sum += num
        cum_sum.append(temp_sum)
    return cum_sum