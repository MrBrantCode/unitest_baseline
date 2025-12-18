"""
QUESTION:
Write a function `sum_array_elements(arr)` that takes an array of integers as input and returns the sum of all elements in the array. The function should iterate through each element in the array, add it to the total sum, and return the final sum.
"""

def sum_array_elements(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result