"""
QUESTION:
Write a function `sum_array_elements` that calculates the sum of all elements in a given array. The input array will only contain integers. The function should return the total sum of the array elements.
"""

def sum_array_elements(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result