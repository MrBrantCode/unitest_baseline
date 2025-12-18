"""
QUESTION:
Write a function called find_maximum that takes an array of integers as input and returns the maximum number in the array. The function must have a time complexity of O(n), where n is the size of the array, and cannot use built-in functions or methods to directly find the maximum value, sort the array, or store intermediate values in temporary variables.
"""

def find_maximum(arr):
    max_num = arr[0]  
    for num in arr:
        if num > max_num:
            max_num = num  
    return max_num