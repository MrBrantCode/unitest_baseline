"""
QUESTION:
Implement a function `find_max_divisible_by_three` that takes an array of integers as input and returns the maximum value in the array that is divisible by 3. If no such value exists, return -1. The function must have a time complexity of O(n) and a space complexity of O(1), and it must not use any built-in sorting or filtering functions.
"""

def find_max_divisible_by_three(arr):
    max_value = -1

    for num in arr:
        if num % 3 == 0:
            if num > max_value:
                max_value = num

    return max_value if max_value != -1 else -1