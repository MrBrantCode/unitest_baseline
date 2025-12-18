"""
QUESTION:
Write a function `find_maximum(arr)` that takes an array of integers as input and returns the maximum number in the array. The function should not use built-in functions or methods to find the maximum value and should not sort the array. The solution should iterate through the array and have a time complexity of O(n). If the array is empty, the function should return negative infinity.
"""

def find_maximum(arr):
    max_num = float('-inf')
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num