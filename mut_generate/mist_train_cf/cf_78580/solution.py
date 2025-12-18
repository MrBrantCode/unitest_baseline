"""
QUESTION:
Write a function `max_sum(arr)` that takes an array of integers as input and returns the maximum sum of four consecutive numbers in the array. The array must have at least four numbers. If the array has less than four numbers, return a message indicating that the array should have at least four numbers.
"""

def max_sum(arr):
    if len(arr) < 4:
        return "Array should have at least four numbers"
    
    max_sum = float('-inf')
    for i in range(len(arr)-3):
        current_sum = sum(arr[i:i+4])
        max_sum = max(max_sum, current_sum)
    return max_sum