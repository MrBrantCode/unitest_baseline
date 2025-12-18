"""
QUESTION:
Write a function `max_sum_without_adjacent` that takes an array of positive integers as input and returns the maximum continuous sum that can be achieved by adding the numbers in the array, excluding any adjacent elements. The function should have a time complexity of O(n) and use constant space.
"""

def max_sum_without_adjacent(arr):
    maxSum = 0
    prevSum = 0

    for num in arr:
        temp = max(num + prevSum, maxSum)
        prevSum = maxSum
        maxSum = temp

    return maxSum