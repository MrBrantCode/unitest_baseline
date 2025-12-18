"""
QUESTION:
Design a function `find_max_value` that takes an array of n integers as input and returns the maximum value considering only the first occurrence of each duplicate value. The function should have a time complexity of O(n) and a space complexity of O(1), and it should only use a single loop to iterate through the array.
"""

def find_max_value(arr):
    max_value = float('-inf')

    for num in arr:
        if num > max_value:
            max_value = num

    return max_value