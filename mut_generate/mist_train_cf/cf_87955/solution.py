"""
QUESTION:
Write a function named `calculate_even_sum` that takes an array of integers as input and returns the sum of all even numbers in the array. The function should use a single loop and have a time complexity of O(n) and a space complexity of O(1). If there are no even numbers in the array, the function should return 0.
"""

def calculate_even_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            sum += arr[i]
    return sum