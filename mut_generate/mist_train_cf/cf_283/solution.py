"""
QUESTION:
Write a function called `find_missing_number` that takes a sorted array of distinct integers as input and returns the single missing number in the array. The missing number is between the minimum and maximum values of the array. The function should have a time complexity of O(n), not O(log n), since the solution provided uses a loop to calculate the sum of the array.
"""

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = (n * (n + 1)) // 2
    arr_sum = sum(arr)
    missing_number = total_sum - arr_sum
    return missing_number