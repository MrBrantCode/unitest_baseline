"""
QUESTION:
Create a function called `is_sum_divisible` that takes an array of integers and an integer `n` as input. The function should return a Boolean indicating whether the sum of the numbers in the array is divisible by `n`. The function must handle negative numbers in the array and have a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1).
"""

def is_sum_divisible(arr, n):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum % n == 0