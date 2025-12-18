"""
QUESTION:
Write a function `maximum_product(arr)` that takes an array of integers as input, sorts it in descending order, and returns the product of the four largest distinct integers. The function should not use any additional data structures and should have a time complexity of O(nlogn), where n is the size of the array.
"""

def maximum_product(arr):
    arr.sort(reverse=True)  # Sort the array in descending order
    maxProduct = arr[0] * arr[1] * arr[2] * arr[3]  # Compute the product of the first four elements
    return maxProduct