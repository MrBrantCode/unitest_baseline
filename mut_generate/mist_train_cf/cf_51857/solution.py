"""
QUESTION:
Write a function `calc_sum(arr)` to calculate the sum of all numbers in the given array, including those in nested arrays. The function should handle arrays of varying depths and return the total sum of all numbers.
"""

def calc_sum(arr):
    total = 0
    for num in arr:
        if isinstance(num, list):
            total += calc_sum(num)
        else:
            total += num
    return total