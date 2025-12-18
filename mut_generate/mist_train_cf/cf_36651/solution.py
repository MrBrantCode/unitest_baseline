"""
QUESTION:
Write a function `f(a)` that takes a list of integers `a` as input and returns the maximum sum of a contiguous subarray within the input list.
"""

def max_subarray_sum(a):
    max_sum = a[0]
    current_sum = a[0]

    for num in a[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum