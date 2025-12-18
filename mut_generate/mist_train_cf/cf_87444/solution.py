"""
QUESTION:
Create a function `is_divisible(arr, n)` that takes an array of integers and an integer `n` as input, and returns a Boolean indicating if the sum of the absolute values of the numbers in the array is divisible by `n`. The function should handle negative numbers in the array and have a time complexity of O(n) and a space complexity of O(1).
"""

def is_divisible(arr, n):
    sum_of_abs = 0
    for num in arr:
        sum_of_abs += abs(num)
    return sum_of_abs % n == 0