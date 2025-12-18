"""
QUESTION:
Write a function named `sum_others` that takes an array of integers as input and returns a new array where each element is the sum of all other elements in the input array except the element at the current index. The function should be able to handle arrays with duplicate integers or zeroes.
"""

def sum_others(arr):
    total_sum = sum(arr)
    sums = []
    for i in arr:
        sums.append(total_sum - i)
    return sums