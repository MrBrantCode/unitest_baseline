"""
QUESTION:
Write a function `sum_even_recursive(arr, index)` that calculates the sum of all even elements in the given array using a recursive approach. The function should take an array `arr` and an integer `index` as parameters and return the sum of even elements. The function should not use any loops and should only use recursive calls. The initial call to the function should be made with `index` set to 0. The function should handle arrays of any length and should return 0 if the array is empty.
"""

def sum_even_recursive(arr, index):
    if index == len(arr):
        return 0

    if arr[index] % 2 == 0:
        return arr[index] + sum_even_recursive(arr, index + 1)
    else:
        return sum_even_recursive(arr, index + 1)