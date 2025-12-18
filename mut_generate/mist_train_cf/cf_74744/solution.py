"""
QUESTION:
Write a function `sum_array(arr)` that calculates the sum of elements in the given array `arr`. The function must use a `for` loop to iterate through the array. The array is 1-dimensional and contains only integers. The function should return the sum of the array elements as an integer. The `for` loop must iterate over the indices of the array, and the array elements should be accessed using their indices.
"""

def sum_array(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum