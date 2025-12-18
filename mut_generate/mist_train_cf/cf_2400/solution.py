"""
QUESTION:
Create a function named `is_divisible` that takes an array of integers and an integer `n` as input and returns a boolean value. The function should calculate the sum of the absolute values of the numbers in the array and return `True` if the sum is divisible by `n`, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1).
"""

def is_divisible(arr, n):
    return sum(abs(num) for num in arr) % n == 0