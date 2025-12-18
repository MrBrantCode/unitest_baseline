"""
QUESTION:
Write a function named `max_sum_digits` that takes a list of integers `arr` and an integer `K` as input, and returns the sum of the `K` largest digits in `arr`. The input list can be in any order and may contain any number of elements, but `K` will always be a positive integer less than or equal to the length of `arr`.
"""

def max_sum_digits(arr, K):
    max_sum = 0
    arr.sort()
    for i in range(K):
        max_sum += arr[len(arr)-1-i]
    return max_sum