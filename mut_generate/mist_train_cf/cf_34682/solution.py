"""
QUESTION:
Write a function `calculate_result(arr, i)` where `arr` is an array of length 2 containing a multiplier and a threshold value, and `i` is a positive integer. The function should calculate the product of `arr[0]` and `i`, and return 0 if the result is less than or equal to `arr[1]`, otherwise return the difference between the product and `arr[1]`.
"""

def entrance(arr, i):
    product = arr[0] * i
    return 0 if product <= arr[1] else product - arr[1]