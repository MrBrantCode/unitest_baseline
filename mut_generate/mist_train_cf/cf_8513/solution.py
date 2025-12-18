"""
QUESTION:
Write a function `product_except_current` that takes an array of numbers as input and returns an array where each element at index `i` is the product of all the numbers in the input array except the number at index `i`. You are not allowed to use division or any built-in multiplication functions in your solution. The input array will always contain at least two elements.
"""

def product_except_current(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    result = [1] * n

    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * arr[i+1]

    for i in range(n):
        result[i] = left[i] * right[i]

    return result