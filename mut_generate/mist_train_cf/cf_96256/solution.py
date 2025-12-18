"""
QUESTION:
Implement a function named find_max that takes an array of numbers as input and returns the maximum number in the array. If the array is empty, return None. Do not use built-in functions or methods to find the maximum number.
"""

def find_max(arr):
    if len(arr) == 0:
        return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num