"""
QUESTION:
Write a function `sum_special(arr)` that takes an array of integers as input and returns the sum of all elements at even indices. The function should use a single loop and achieve a time complexity of O(n).
"""

def sum_special(arr):
    total_sum = 0
    for i in range(0, len(arr), 2):
        total_sum += arr[i]
    return total_sum