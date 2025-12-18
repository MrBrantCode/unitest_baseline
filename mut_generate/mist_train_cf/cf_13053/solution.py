"""
QUESTION:
Write a function named `sum_even_recursive` that takes in an array and an index as parameters and returns the sum of all even elements in the array using a recursive approach. The function should start from the given index and traverse the array, adding up all the even elements. The function should handle arrays of varying lengths and compositions.
"""

def sum_even_recursive(arr, index):
    if index == len(arr):
        return 0

    if arr[index] % 2 == 0:
        return arr[index] + sum_even_recursive(arr, index + 1)
    else:
        return sum_even_recursive(arr, index + 1)