"""
QUESTION:
Create a function named `is_sum_divisible` that takes an array of integers `arr` and an integer `n` as input, and returns a boolean indicating whether the sum of the numbers in `arr` is divisible by `n`. The function should be able to handle negative numbers in the array and must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

def is_sum_divisible(arr, n):
    total_sum = 0
    
    for num in arr:
        total_sum += num
    
    return total_sum % n == 0